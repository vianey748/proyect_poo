from rest_framework.decorators import api_view
from rest-framework.response import Response
from .serializers import UsersSerializer

user = {
    "name": "Vianeyl",
    "password": "123"
}

@api_view(["GET"])
def get_users(request):
    return Response(UserSerializer(user).data)


# Create your views here.
