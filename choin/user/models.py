from django.db import models

# Create your models here.
class emails(models.Model):
    student_emails =models.FileField(upload_to='')