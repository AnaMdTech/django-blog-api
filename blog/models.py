from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    content = models.TextField()
    img = models.URLField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
