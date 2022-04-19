from this import d
from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class SoloAdminPuedeEscribir(BasePermission):
    def has_permission(self, request: Request, views):
        print(request.user)
        return True
