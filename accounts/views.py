from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .models import Account


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"error": "Email and password required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        if not check_password(password, user.password):
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)  # works even with custom user if you subclass AbstractBaseUser

        return Response({
            "message": "Login successful",
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "email": user.email,
                "role": user.role
            }
        }, status=status.HTTP_200_OK)
