from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import CreateAPIView
from .serializers import TokenSerializer
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.contrib.auth import get_user_model


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny    # Or anon users can't register
    ]
    serializer_class = UserSerializer


class UserToken(APIView):
    """
    If user is Authenticated response his token.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        token = get_object_or_404(Token, user=request.user)
        data = TokenSerializer(token).data
        return Response(data, status=status.HTTP_201_CREATED)
