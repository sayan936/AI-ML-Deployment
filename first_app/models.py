from django.db import models


# Create your models here.
class PredictionLog(models.Model):
    request_data = models.TextField()  # Or any other fields relevant to your request
    prediction_result = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction made on {self.created_at}"