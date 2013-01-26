from django.contrib.auth.models import User

from rest_framework.authentication import BasicAuthentication
from rest_framework.mixin import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

from .models import Entry
from .serializers import EntrySerializer, UserSerializer


class EntryEndpoint(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    model = Entry
    serializer_class = EntrySerializer


class UserEndpoint(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    model = User
    serializer_class = UserSerializer

