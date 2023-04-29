from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, CategoryViewSet, GenreViewSet, TitleViewSet,
    ReviewViewSet, CommentViewSet, SignUpViewSet, GetTokenViewSet
)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register('users', UserViewSet, basename='users')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register('genres', GenreViewSet, basename='genres')
urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', SignUpViewSet.as_view(), name='signup'),
    path('v1/auth/get-token/', GetTokenViewSet.as_view(), name='get-token'),
]
