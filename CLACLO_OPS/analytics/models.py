from django.db import models
from surveys.models import Survey

class AnalysisReport(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    report_data = models.JSONField()

    def __str__(self):
        return f"Analysis for {self.survey.title}"
