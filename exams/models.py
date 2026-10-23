from django.db import models

from accounts.models import User

class Assessment(models.Model):

    title = models.CharField(max_length=200)

    batch = models.CharField(max_length=200)

    LANGUAGE_CHOICES = (
        ("python","python"),
        ("react","react"),
        ("html","html"),
        ("css","css"),
        ("javascript","javascript")
    )

    language = models.CharField(max_length=200,choices=LANGUAGE_CHOICES)

    exam_date = models.DateField(null=False)

    start_time = models.TimeField(null=False)

    duration = models.PositiveIntegerField(null=False)

    end_time = models.TimeField(null=True)

    STATUS_CHOICES = (
        ("pending","pending"),
        ("ongoing","ongoing"),
        ("completed","completed"),
        ("submitted","submitted")
    )

    status = models.CharField(max_length=200,choices=STATUS_CHOICES,default="pending")

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
