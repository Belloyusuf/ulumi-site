from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related
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



# COMMENT SYSTEM
class Comment(models.Model):
    help_text = "user's comments"
    news = models.ForeignKey(News, on_delete=models.CASCADE,
                            related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField(help_text='We like to hear from you')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.news}'