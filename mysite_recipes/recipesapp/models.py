from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    steps_cooking = models.TextField()
    time_for_cooking = models.IntegerField(default=10)
    photo = models.ImageField(upload_to="img/%Y/%m/%d/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Рецепты'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipes-detail', kwargs={'pk': self.pk})

    # def save(self):
    #     super().save()
    #
    #     img = Image.open(self.photo.path)
    #     if img.height > 300 or img.width >300:
    #         new_img = (300, 300)
    #         img.thumbnail(new_img)
    #         img.save(self.photo.path)


# Create your models here.
