from django.db import models


# Create your models here.
class ContactUs(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=120)
    message = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Contact Us"
        ordering = ["-created_at"]

    def __str__(self):
        return self.first_name + " " + self.last_name
    

class GetInTouch(models.Model):
    phone = models.CharField(max_length=230)
    email = models.EmailField()
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Get In Touch"

    def __str__(self):
        return self.phone