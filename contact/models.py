from django.db import models
from phone_field import PhoneField
from django.contrib.auth import get_user_model
User = get_user_model()


class Contact(models.Model):
    Name = models.CharField(max_length=255)
    Phone_number = PhoneField()
    Email = models.EmailField(blank=True)
    Marked_Spam_no = models.PositiveIntegerField(default=0)
    Marked_by = models.ManyToManyField(User, blank=True, related_name="marked_by_these_many_peoples")
    In_List = models.ManyToManyField(User, blank=True, related_name="from_person_contact_list")
    Registered_user = models.BooleanField(default=False)

    def __str__(self):
        return self.Name
