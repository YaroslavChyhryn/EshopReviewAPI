from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.utils.translation import gettext_lazy


class ShopModel(models.Model):
    domain = models.CharField(max_length=64, unique=True, blank=False)


class ReviewModel(models.Model):
    shop_link = models.URLField(max_length=255, blank=True)
    shop = models.ForeignKey(ShopModel, related_name='reviews', on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reviews', on_delete=models.CASCADE)
    title = models.CharField(max_length=64, blank=True)
    description = models.CharField(max_length=550, blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name = gettext_lazy('review')
        verbose_name_plural = gettext_lazy('reviews')
        ordering = ['-created']
