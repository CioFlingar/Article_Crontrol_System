from django.contrib import admin

from .models import Articles, UserProfile


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "word_count", "created_at", "updated_at")
    list_filter = ("status",)
    search_fields = ("title", "content")
    date_hierarchy = "created_at"
    ordering = ("created_at",)
    readonly_fields = ("word_count", "created_at", "updated_at")


admin.site.register(UserProfile)
admin.site.register(Articles, ArticleAdmin)
