from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxLengthValidator


class Feedback(models.Model):
    full_name = models.CharField(max_length=100)
    number = PhoneNumberField(validators=[MaxLengthValidator(20)])
    email = models.EmailField()
    contact_method = models.CharField(max_length=100, null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
