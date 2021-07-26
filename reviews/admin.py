from django.contrib import admin
from .models import ReviewModel


@admin.register(ReviewModel)
class ReviewAdmin(admin.ModelAdmin):
    pass
