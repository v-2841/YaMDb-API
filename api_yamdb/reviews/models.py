from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    ROLES = (
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    )
    email = models.EmailField(unique=True, blank=False, null=False)
    role = models.CharField(
        choices=ROLES,
        blank=False,
        null=False,
        default='user',
        max_length=20,
    )
    bio = models.TextField(blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1900),
                    MaxValueValidator(datetime.now().year + 20),
                    ]
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='titles',
    )
    genre = models.ManyToManyField(Genre, through='GenreTitle')


class GenreTitle(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    text = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    score = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1),
                    MaxValueValidator(10),
                    ]
    )
    pub_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField(blank=False, null=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    pub_date = models.DateTimeField(auto_now_add=True)
