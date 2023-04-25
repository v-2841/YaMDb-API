from django.contrib import admin

from .models import (
    User, Title, Category, Genre, GenreTitle,
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


admin.site.register(User, UserAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(GenreTitle)
admin.site.register(Review)
admin.site.register(Comment)
