from rest_framework.permissions import BasePermission


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # allow user to list all users if logged in user is staff
        return request.method in ('GET',) or request.user.is_staff


class IsStaffOrTargetUser(BasePermission):
    def has_permission(self, request, view):
        # allow user to list all users if logged in user is staff
        return view.action == 'retrieve' or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # allow logged in user to view own details, allows staff to view all records
        return request.user.is_staff or obj == request.user

