from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers

# login serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150,
        required=True,
        help_text="Enter your username"
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        help_text="Enter your password"
    )

# register serializer

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True) 
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    # Validate password match
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match"})
        return attrs

    # Create user
    def create(self, validated_data):
        validated_data.pop('confirm_password') 
        return User.objects.create_user(**validated_data)

# Serializer for Request OTP
class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

# Serializer for Verify OTP and Reset Password
class ResetPasswordSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return attrs
