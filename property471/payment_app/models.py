from django.db import models
from property_app.models import property
from signup_login_app.models import user, employee
from .models import *


# Create your models here.
class transaction(models.Model):
    transaction_id = models.CharField(max_length=50, primary_key=True)

    buyer_id = models.CharField(max_length=50)
    seller_id = models.CharField(max_length=50)
    agent_id = models.CharField(max_length=50)
    property_id = models.CharField(max_length=50)

    buyer_sends = models.CharField(max_length=50)
    seller_receives = models.CharField(max_length=50)
    agent_receives = models.CharField(max_length=50)
