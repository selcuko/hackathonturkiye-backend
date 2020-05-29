from rest_framework.permissions import BasePermission


class IsBlacklisted(BasePermission):
    """
    Global website access prohibiton.
    Birazdan implemente edilecek
    """

    def has_permission(self, request, view):
        return True


class IsPOST(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        else:
            return False