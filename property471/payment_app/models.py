from django.db import models
from property_app.models import property
from signup_login_app.models import user, employee


# Create your models here.
class transaction(models.Model):
    transaction_id = models.CharField(max_length=50, primary_key=True)

    buyer_id = models.ForeignKey(
        user,
        to_field="user_id",
        on_delete=models.CASCADE,
        related_name="property_buyer_id",
    )
    seller_id = models.ForeignKey(
        user,
        to_field="user_id",
        on_delete=models.CASCADE,
        related_name="property_seller_id",
    )
    agent_id = models.ForeignKey(
        user,
        to_field="user_id",
        on_delete=models.CASCADE,
        related_name="property_agent_id",
    )
    admin_id = models.ForeignKey(
        user,
        to_field="user_id",
        on_delete=models.CASCADE,
        related_name="property_admin_id",
    )
    property_id = models.ForeignKey(
        property, to_field="property_id", on_delete=models.CASCADE
    )

    buyer_sends = models.CharField(max_length=50)
    seller_receives = models.CharField(max_length=50)
    agent_receives = models.CharField(max_length=50)
