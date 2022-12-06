from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):  #просматривать может каждый, удалять - администратор
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # проверка запроса на безопасность
           return True

        return bool(request.user and request.user.is_staff)# иначе доступ только для админа


class IsOwnerOrReadOnly(permissions.BasePermission): #изменять запись может только автор, просмотр - все
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # проверка запроса на безопасность
           return True
        return obj.user == request.user
