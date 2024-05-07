from django.db import models

class LogEntry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f"LogEntry {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
