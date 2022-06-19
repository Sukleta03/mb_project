from django.db import models


class Post(models.Model):
    text = models.TextField()


    def __str__(self):
        """название модели == первые 50 символов модели"""
        return self.text[:20]
