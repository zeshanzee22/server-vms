
# Create your models here.
from django.db import models


class Account(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    id = models.AutoField(primary_key=True)  # <-- replace userID with id
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_'):
            from django.contrib.auth.hashers import make_password
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
    

class DeviceType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class AlertType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    id = models.AutoField(primary_key=True)  # roomid
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    qr_info = models.TextField(blank=True, null=True)  # can store QR code data or link
    created_at = models.DateTimeField(auto_now_add=True)  # when the room was created

    def __str__(self):
        return f"{self.name} (ID: {self.id})"

class WarningType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



class Device(models.Model):
    name = models.CharField(max_length=100,null=True)
    mac_adress = models.CharField(max_length=30,unique=True,db_index=True)
    imei = models.CharField(max_length=30,unique=True,db_index=True)
    
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name