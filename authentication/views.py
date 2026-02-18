from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from .serializers import ForgetPasswordSerializer, ResetPasswordSerializer
from django.core.mail import send_mail
from .models import PasswordResetOTP
import random
from django.contrib.auth.models import User


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
    return Response({"message": "User Registered Successfully"}, status=status.HTTP_201_CREATED)

# forget View

class ForgetPasswordView(APIView):
    def post(self, request):
        serializer = ForgetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first()

        if not user:
            return Response({"error": "User not found"}, status=404)

        # Delete old OTP
        PasswordResetOTP.objects.filter(user=user).delete()
        otp = str(random.randint(100000, 999999))
        PasswordResetOTP.objects.create(user=user, otp=otp)
        send_mail(
            "Password Reset OTP",
            f"Your OTP is {otp}",
            "your_email@gmail.com",
            [email],
        )
        return Response({"message": "OTP sent successfully"})


# reset password view
class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        otp = serializer.validated_data['otp']
        new_password = serializer.validated_data['new_password']

        # Find OTP object
        otp_obj = PasswordResetOTP.objects.filter(otp=otp).first()
        if not otp_obj or otp_obj.is_expired():
            return Response({"error": "Invalid or expired OTP"}, status=400)

        # Get user from OTP object
        user = otp_obj.user
        user.set_password(new_password)
        user.save()

        # Delete OTP after use
        otp_obj.delete()

        return Response({"message": "Password reset successful"})
