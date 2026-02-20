from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from snippets.auth_serializers import RegisterSerializer


class UserRegistrationApi(generics.CreateAPIView):
    """
    API endpoint for user registration.
    Accepts POST requests with user registration data and creates a new user.
    Returns a response containing the registered user's data and JWT tokens.
    """
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            "user": serializer.data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
