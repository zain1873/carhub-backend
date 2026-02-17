from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password) 
        if not user:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        token = RefreshToken.for_user(user)
        return Response({
            "message": "Login successful",
            "access": str(token.access_token),
            "refresh": str(token)
        })

# registerView

class RegisterView(APIView):
  def post(self, request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

        
        
    