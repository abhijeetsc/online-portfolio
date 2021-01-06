from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=500)
    pub_date = models.DateTimeField()
    body = models.TextField()
    blog_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        summary = self.body[:300]
        summary += '...'
        return summary
