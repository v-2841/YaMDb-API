from rest_framework import viewsets, pagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator

from .permissions import (IsAdminOrReadOnly, IsAdminOrModeratorOrReadOnly,
    IsAuthorOrModeratorOrAdminOrReadOnly, IsAuthorOrReadOnly)

from .serializers import (UserSerializer, CategorySerializer, GenreSerializer,
                          TitleSerializer, ReviewSerializer, CommentSerializer,
                          SignUpSerializer, TokenSerializer)
from reviews.models import User, Category, Genre, Title, Review, Comment


from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 10


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPageNumberPagination


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPageNumberPagination


class GenreViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = CustomPageNumberPagination


class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    pagination_class = CustomPageNumberPagination


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = CustomPageNumberPagination


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CustomPageNumberPagination


class SignUpViewSet(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        confirmation_code = default_token_generator.make_token(user)
        email = request.data.get('email')
        send_mail(
            'Код подтверждения',
            f'Ваш код: {confirmation_code}',
            from_email=None,
            recipient_list=[email]
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetTokenViewSet(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        confirmation_code = serializer.validated_data.get('confirmation_code')
        user = get_object_or_404(
            User,
            username=username,
        )
        if user.confirmation_code != confirmation_code:
            return Response(
                'Неправильный код подтверждения',
                status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)
        return Response(
            {'access_token': str(refresh.access_token)},
            status=status.HTTP_200_OK
        )
