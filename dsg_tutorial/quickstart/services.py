from django_socio_grpc import generics

from quickstart.models import User, Post
from quickstart.serializers import UserProtoSerializer, PostProtoSerializer

class UserService(generics.ReadOnlyModelService):
    # list, retrieve
    queryset = User.objects.all()
    serializer_class = UserProtoSerializer

class PostService(generics.AsyncModelService):
    # list, retrieve, create, update, partial_update, destroy
    queryset = Post.objects.all()
    serializer_class = PostProtoSerializer
