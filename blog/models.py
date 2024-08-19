from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=500)
    body = models.TextField()
    image = models.ImageField(upload_to='posts/')
    category = models.ForeignKey(Category, models.SET_NULL, null=True, blank=True)
    editors_pick = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    hit_count = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title