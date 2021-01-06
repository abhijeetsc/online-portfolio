from django.db import models


class Jobs(models.Model):
    job_image = models.ImageField(upload_to='images/')
    job_desc = models.CharField(max_length=200)
