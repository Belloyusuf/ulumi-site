from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique_for_date='written')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    written = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 


    class Meta:
        ordering = ['-title']


    def get_absolute_url(self):
        return reverse('full_detail',
                        args=[
                            self.written.year,
                            self.written.month,
                            self.written.day,
                            self.slug
                        ])

