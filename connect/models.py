from django.db import models


class Review(models.Model):
    username = models.CharField(max_length=150)
    description = models.TextField(max_length=550)
    grade = models.IntegerField(default=0)

    def __str__(self):
        return f"username: {self.username}"
