from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CommentList, ReviewList, TitleList,
                    GenreList, CategoryList, SignUpView,
                    GetTokenView)


router_v1 = DefaultRouter()
router_v1.register('title', TitleList)
router_v1.register('genre', GenreList)
router_v1.register('category', CategoryList)
router_v1.register(
    r'titles/(?P<title_id>[\d]+)/reviews',
    ReviewList,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>[\d]+)/reviews/(?P<review_id>[\d]+)/comments',
    CommentList,
    basename='comments',
)
urlpatterns = [
    path('v1/auth/signup/', SignUpView.as_view(), name='sign_up'),
    path('v1/auth/token/', GetTokenView.as_view(), name='get_token'),
    path('v1/', include(router_v1.urls)),
]
