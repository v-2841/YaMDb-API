from django.contrib import admin

from .models import (
    User, Title, Category, Genre,
    Review, Comment
)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'year',
        'category',
        'description',
    )
    search_fields = ('name',)
    list_filter = (
        'category',
    )


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'email',
    )
    search_fields = ('text',)
    list_filter = ('role',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'author',
        'score',
    )


admin.site.register(User, UserAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment)
