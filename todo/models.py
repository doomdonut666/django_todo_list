from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=500, verbose_name='task name')
    description = models.TextField(blank=True, verbose_name='Task description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    completed = models.BooleanField(default=False, verbose_name='Completed or not')

def __str__(self):
    return self.title
