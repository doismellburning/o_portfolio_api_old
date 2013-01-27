from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Entry
from .serializers import EntrySerializer, RegistrationSerializer, UserSerializer


class APIAuthMixin(object):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class EntryEndpoint(APIAuthMixin, RetrieveUpdateDestroyAPIView):
    model = Entry
    serializer_class = EntrySerializer

    def get_object(self, *args, **kwargs):
        obj = super(EntryEndpoint, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj


class EntryListEndpoint(APIAuthMixin, ListCreateAPIView):
    model = Entry
    serializer_class = EntrySerializer

    def get_queryset(self, *args, **kwargs):
        qs = super(EntryListEndpoint, self).get_queryset(*args, **kwargs)
        return qs.filter(user=self.request.user)

    def pre_save(self, obj):
        obj.user = self.request.user


class UserEndpoint(APIAuthMixin, RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer

    def get_object(self, queryset=None):
        return self.request.user


class UserRegistrationEndpoint(CreateAPIView):
    model = User
    serializer_class = RegistrationSerializer

