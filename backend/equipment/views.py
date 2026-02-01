import pandas as pd
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Dataset
from .analytics import analyze
from .insights import generate_insights
from .validators import validate_csv


@api_view(["POST"])
@permission_classes([AllowAny])
@permission_classes([AllowAny])
def upload_csv(request):
    file = request.FILES.get("file")
    if not file:
        return Response(
            {"error": "CSV file required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        df = pd.read_csv(file)
    except Exception:
        return Response(
            {"error": "Invalid CSV file"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Validate CSV structure
    try:
        validate_csv(df)
    except ValueError as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Analyze data
    summary = analyze(df)
    insights = generate_insights(summary)

    # Save dataset
    Dataset.objects.create(
        filename=file.name,
        summary=summary,
        insights=insights
    )

    # Keep only last 5 uploads (SAFE METHOD)
    dataset_ids = list(
        Dataset.objects
        .order_by("-uploaded_at")
        .values_list("id", flat=True)
    )

    if len(dataset_ids) > 5:
        Dataset.objects.filter(id__in=dataset_ids[5:]).delete()

    # ✅ RETURN RESPONSE (CRITICAL)
    return Response(
        {
            "summary": summary,
            "insights": insights
        },
        status=status.HTTP_200_OK
    )