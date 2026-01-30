from django.db import models

class Dataset(models.Model):
    filename = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    summary = models.JSONField()
    insights = models.JSONField()

    def __str__(self):
        return self.filename