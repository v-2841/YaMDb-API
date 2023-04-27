from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CommentList, ReviewList, TitleList,
                    GenreList, CategoryList, SignUpView,
                    GetTokenView)

app_name = 'api'

router = DefaultRouter()

router.register('tittle', TitleList)
router.register('genre', GenreList)
router.register('category', CategoryList)

router.register(
    r'titles/(?P<title_id>[\d]+)/reviews',
    ReviewList,
    basename='reviews'
)

router.register(
    r'titles/(?P<title_id>[\d]+)/reviews/(?P<review_id>[\d]+)/comments',
    CommentList,
    basename='comments',
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', SignUpView.as_view(), name='sign_up'),
    path('v1/auth/token/', GetTokenView.as_view(), name='get_token'),
]
