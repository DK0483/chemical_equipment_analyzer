def generate_insights(summary):
    insights = []

    insights.append(
        f"{summary['total_equipment']} equipment units analyzed."
    )

    if summary["alerts"]:
        insights.append(
            f"{len(summary['alerts'])} units exceeded safe limits."
        )
    else:
        insights.append(
            "All equipment are operating safely."
        )

    return insights