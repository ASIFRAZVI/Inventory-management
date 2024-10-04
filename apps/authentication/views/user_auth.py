from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth.hashers import make_password, check_password
from inventory_management.settings.config import JWT_SECRET
from apps.authentication.helpers.password_generator import password_generator

from apps.authentication.models.user_auth import CustomUser
from apps.authentication.jwt_processor.jwt_generator import (
    generate_jwt_token,
    generate_refresh_token,
)
from apps.authentication.jwt_processor.jwt_decoder import decode_jwt_token
from apps.authentication.serializers.user_auth_serializer import (
    auth_serializer,
    login_serializer,
)

jwt_secret = JWT_SECRET


class Registration(APIView):
    """Register a new user."""

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user_serializer = auth_serializer(data=request.data)

        if not user_serializer.is_valid():
            return Response(
                {"errors": "Please provide unique email"},
                status=400,
            )

        email = user_serializer.validated_data["email"]
        password = password_generator(15)
        hashed_password = make_password(password)
        if CustomUser.objects.filter(email=email).exists():
            return Response(
                {"error": "A user with this email already exists."},
                status=400,
            )

        user_data = {
            "email": email,
            "password": hashed_password,
        }

        user = CustomUser.objects.create(**user_data)
        user.save()
        return Response(
            {"email": email, "password": password}, status=status.HTTP_201_CREATED
        )


class Login(APIView):
    """Function to login user"""

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        signin_serializer = login_serializer(data=request.data)

        if signin_serializer.is_valid():
            email = signin_serializer.validated_data.get("email")
            password = signin_serializer.validated_data.get("password")

            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return Response(
                    {"error": "Invalid Email, please provide valid email"}, status=400
                )

            if check_password(password, user.password):
                # generate access main token
                jwt_token = generate_jwt_token(user.id, jwt_secret)

                # Generate refresh token
                refresh_token = generate_refresh_token(user.id, jwt_secret)

                response = Response(
                    {
                        "token": jwt_token,
                        "refresh_token": refresh_token,
                        "ok": "cookies stored!",
                    },
                    status=200,
                )

                # Set token in cookies
                response.set_cookie("access_token", jwt_token, httponly=True)
                response.set_cookie("refresh_token", refresh_token, httponly=True)

                return response

            else:
                return Response({"error": "wrong password!"}, status=400)

        else:
            return Response(
                signin_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class Logout(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [decode_jwt_token]

    def post(self, request):
        response = Response({"message": "Logged out successfully."}, status=200)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response
