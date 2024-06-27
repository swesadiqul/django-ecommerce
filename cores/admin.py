from django.contrib import admin
from cores.models import *


# Register your models here.
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    pass


@admin.register(GetInTouch)
class GetInTouchAdmin(admin.ModelAdmin):
    pass