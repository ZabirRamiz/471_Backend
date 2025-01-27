from django.db import models
from signup_login_app.models import user, employee

# from payment_app.models import admin_earning

# Create your models here.


class property(models.Model):
    property_id = models.CharField(max_length=50, primary_key=True)

    user_id = models.ForeignKey(
        user,
        to_field="user_id",
        related_name="property_owner",
        on_delete=models.CASCADE,
    )

    # # had to add the related_name attribute to distinguish the foreign keys to avoid clash
    agent_id = models.ForeignKey(
        employee,
        to_field="employee_id",
        related_name="property_agent",
        on_delete=models.SET_NULL,
        null=True,
    )
    support_id = models.ForeignKey(
        employee,
        to_field="employee_id",
        related_name="property_support",
        on_delete=models.SET_NULL,
        null=True,
    )

    market_status = models.CharField(default="Available For Sale", max_length=50)
    property_location = models.CharField(max_length=500)
    property_size = models.CharField(max_length=50)
    property_name = models.CharField(max_length=50)
    property_price = models.CharField(max_length=50)
    admin_approval = models.CharField(max_length=50, null=True)
    buyer_id = models.ForeignKey(
        user,
        to_field="user_id",
        related_name="property_buyer",
        on_delete=models.SET_NULL,
        null=True,
    )

    # def __str__(self):
    #     return f"property_id = {self.property_id}, owner_id = {self.owner_id}, agent_id = {self.agent_id}, support_id = {self.support_id}"
