from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.role in ['admin']:
            return True

        return False


class IsAuthorOrModeratorOrAdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if (
            request.user.is_authenticated
            and request.user.role in ['admin', 'moderator']
        ):
            return True

        if obj.author == request.user:
            return True

        return False
