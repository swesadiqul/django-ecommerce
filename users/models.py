from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField



class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if email:
            email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    agree_to_terms = models.BooleanField(default=False, verbose_name="Agree to Terms and Privacy")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.full_name or self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to="profile", default='profile/user.png')
    dob = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    country = CountryField(blank_label="-- Select Country-- ", default='BD')
    city = models.CharField(max_length=100, blank=True, null=True)
    post_code = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.full_name

    class Meta:
        verbose_name_plural = "Profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

User = get_user_model()
post_save.connect(create_profile, sender=User)