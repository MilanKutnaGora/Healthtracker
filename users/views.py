from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        data = serializer.save()
        new_user = User.objects.get(pk=data.pk)
        new_user.set_password(data.password)
        new_user.save()