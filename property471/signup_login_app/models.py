from django.db import models


# Create your models here.
def upload_to(instance, filename):
    return "media/{filename}".format(filename=filename)


class user(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    type = models.CharField(default="user", max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    wallet = models.CharField(max_length=50, default=1000000)
    session_id = models.CharField(default=-1, max_length=50)

    user_image = models.ImageField(
        upload_to="user_image", default="media/stock_user.jpg"
    )
    user_image_path = models.CharField(
        max_length=5000, default="/user_image/default_user_image.jpg"
    )

    # user_image = models.ImageField(null = True)
    # user_image = models.CharField(null=True, max_length=50)
    # def __str__(self):
    #     return f"user_id: {self.user_id}, password: {self.password}"
    # def __str__(self):
    #     return self.user_image


class session(models.Model):
    session_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user, to_field="user_id", on_delete=models.CASCADE)
    status = models.CharField(default="False", max_length=5)

    def __str__(self):
        return f"session_id: {self.session_id}, {self.user_id}, status: {self.status}"


class employee(models.Model):
    employee_id = models.ForeignKey(
        user,
        to_field="user_id",
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="employee_id",
    )
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    wallet = models.CharField(max_length=50, default=1000000)
    hiring_price = models.CharField(max_length=50, default=20)
    commission = models.CharField(max_length=50, default=5)

    def __str__(self):
        return f"employee_id: {self.employee_id}, password: {self.password}"
