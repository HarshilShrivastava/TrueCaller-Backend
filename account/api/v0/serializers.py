from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta():
        model = User
        fields = ['email', 'password', 'confirm_password', 'first_name', 'last_name', 'phone_number', 'Is_User']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = User(
            email=self.validated_data['email'].lower(),
            Is_User=self.validated_data['Is_User'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Password must match.'})
        account.set_password(password)
        account.phone_number = self.validated_data['phone_number']
        account.save()
        return account


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=20)

    class Meta:
        fields = ['username', 'password']
