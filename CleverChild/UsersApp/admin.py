from django.contrib import admin

# Register your models here.
from .models import Parent, Child, Specialist

admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(Specialist)

