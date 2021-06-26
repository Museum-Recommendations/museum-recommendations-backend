from django.contrib import admin

# Register your models here.

from .models import UserReview


@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
	pass