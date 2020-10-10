from contact.models import Contact
from rest_framework import serializers


class contactserializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['Name', 'Phone_number', 'Marked_Spam_no', 'Registered_user', 'id']


class contact1serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['Name', 'Phone_number', 'Marked_Spam_no', 'Registered_user', 'Email', 'id']
