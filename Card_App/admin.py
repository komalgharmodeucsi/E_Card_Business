from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Member, Design, Person

admin.site.register(Member)
admin.site.register(Design)
admin.site.register(Person)
