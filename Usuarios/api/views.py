from rest_framework import generics
from ..models import Users
from .serializers import UsersSerializer

class Listado(generics.ListAPIView):
	permissions_classes = ()
	queryset = Users.objects.all()
	serializer_class = UsersSerializer