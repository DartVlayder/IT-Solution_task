from django.db import models

class Quote(models.Model):
    text = models.TextField(unique=True)
    source = models.CharField()
    weight = models.PositiveIntegerField(default=1)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text} из {self.source}'