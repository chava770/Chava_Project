from django.contrib import admin
from .models import Workers, Job, Paradigm

# Unregister the model if it's already registered
try:
    admin.site.unregister(Workers)
except admin.sites.NotRegistered:
    pass

# Register your models here.
admin.site.register(Workers)
admin.site.register(Job)
admin.site.register(Paradigm)
