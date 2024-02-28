from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    subject = models.CharField(max_length=212)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    address = models.CharField(max_length=212)
    opening_hours = models.CharField(max_length=212)
    phone = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address


class GetInTouch(models.Model):
    name = models.CharField(max_length=212)
    phone = models.CharField(max_length=212)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
