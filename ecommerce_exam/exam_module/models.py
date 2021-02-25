from django.db import models

class LabExam(models.Model):
# Create your models here.
    exam_date = models.DateTimeField()
    exam_name = models.CharField(max_length=20)
    exam_description = models.CharField(max_length=500)
    total_marks = models.FloatField()
    pass_marks = models.FloatField()
    exam_status = models.BooleanField()

    def __str__(self):
        return self.exam_name