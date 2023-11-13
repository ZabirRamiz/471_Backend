from django.db import models

# Create your models here.


class user(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    type = models.CharField(default = 'user',max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    session_id = models.CharField(default = -1, max_length=50)

    def __str__(self):
        return f"user_id: {self.user_id}, password: {self.password}"
    
class session(models.Model):
    session_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(user, to_field = 'user_id', on_delete=models.CASCADE)
    status = models.CharField(default = "False", max_length=5)

    def __str__(self):
        return f"session_id: {self.session_id}, {self.user_id}, status: {self.status}"


class employee(models.Model):
    employee_id = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    

    def __str__(self):
        return f"employee_id: {self.employee_id}, password: {self.password}"
