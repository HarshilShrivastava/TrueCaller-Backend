from .views import registration_view, ObtainAuthTokenView
from django.urls import path

app_name = 'Account_api'
urlpatterns = [
    path('registration/', registration_view, name="registration"),
    path('login/', ObtainAuthTokenView, name="login"),

]
