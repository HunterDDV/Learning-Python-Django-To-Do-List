from django.db import models

class Task(models.Model):
    # id = 
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.name

class Meta:
    ordering = ['created_at']