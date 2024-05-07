from django.db import models

class University(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    activation_date = models.DateTimeField(null=True, blank=True)
    deactivation_date = models.DateTimeField(null=True, blank=True

    def __str__(self):
        return self.name

class Department(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.university.name}"
