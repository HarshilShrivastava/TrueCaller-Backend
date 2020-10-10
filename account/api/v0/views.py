from django.contrib.auth import get_user_model
User = get_user_model()
from contact.models import Contact
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .serializers import (
    RegistrationSerializer,
    LoginSerializer
)


@api_view(['POST', ])
@permission_classes((AllowAny,))
def registration_view(request):
    if request.method == 'POST':
        data = {}
        context = {}
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            context['success'] = True
            context['message'] = 'Successfully registered'
            context['status'] = status.HTTP_201_CREATED
            data['phone_number'] = user.phone_number
            token = Token.objects.create(user=user).key
            obj=Contact.objects.create(Phone_number=user.phone_number,Name=user.get_full_name(),Email=user.email,Registered_user=True)
            obj.save()
            data['token'] = token
            context['data'] = data
        else:
            context['success'] = False
            context['response'] = status.HTTP_400_BAD_REQUEST
            context['message'] = 'not registered registered'
            data = serializer.errors
            context['error_message'] = data
    return Response(context)


@api_view(['POST', ])
@permission_classes((AllowAny,))
def ObtainAuthTokenView(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        context = {}
        data = {}
        if serializer.is_valid(raise_exception=True):
            usernam = serializer.validated_data['phone_number']
            passwor = serializer.validated_data['password']
            print(usernam,passwor)
            account = authenticate(phone_number=usernam, password=passwor)
            print(account)
            if account:
                try:
                    token = Token.objects.get(user=account)
                except Token.DoesNotExist:
                    token = Token.objects.create(user=account)
                context['response'] = 200
                context['success'] = True
                context['error_message'] = "successful login"
                data['token'] = token.key
                #data['username'] = account.phone_number
                data['email'] = account.email
                data['id'] = account.id
                context['data'] = data
            else:
                context['success'] = False
                context['status']: 440
                context['response'] = 'Error'
                context['error_message'] = 'Invalid credentials'
        return Response(context)
