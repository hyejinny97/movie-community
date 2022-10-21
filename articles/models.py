from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    movie_name = models.CharField(max_length=80)
    grade = models.FloatField(default=3.0, validators=[MinValueValidator(1.0),MaxValueValidator(5.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, upload_to='images/')
    thumbnail = ProcessedImageField(upload_to='thumbnails/',
                                         blank=True,
                                         processors=[Thumbnail(300, 150)],
                                         format='JPEG',
                                         options={'quality': 100})
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    review = models.ForeignKey("Article", on_delete=models.CASCADE)
    content = models.CharField(max_length=130)
    created_at = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)