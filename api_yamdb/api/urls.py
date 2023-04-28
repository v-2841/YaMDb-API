from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UserList, UserDetail, CategoryList, CategoryDetail,
                    GenreList, GenreDetail, TitleList, TitleDetail,
                    ReviewList, ReviewDetail, CommentList, CommentDetail,
                    SignUpView, GetTokenView)

router_v1 = DefaultRouter()
router_v1.register('users', UserList, basename='user')
router_v1.register('categories', CategoryList, basename='category')
router_v1.register('genres', GenreList, basename='genre')
router_v1.register('titles', TitleList, basename='title')
router_v1.register('reviews', ReviewList, basename='review')
router_v1.register('comments', CommentList, basename='comment')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('categories/<int:pk>/',
         CategoryDetail.as_view(),
         name='category-detail'),
    path('genres/<int:pk>/', GenreDetail.as_view(), name='genre-detail'),
    path('titles/<int:pk>/', TitleDetail.as_view(), name='title-detail'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('get-token/', GetTokenView.as_view(), name='get-token'),
]
