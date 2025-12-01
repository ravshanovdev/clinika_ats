from django.db import models


class Review(models.Model):
    username = models.CharField(max_length=150)
    description = models.TextField()
    grade = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"username: {self.username}"
