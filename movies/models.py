from django.db import models
from user.models import User

class Movie(models.Model):
    url = models.CharField(max_length=512, default="")
    title = models.CharField(max_length=255, default="", blank=True)
    description = models.TextField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "movies"
