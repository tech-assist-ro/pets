from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Pet, ShelterProfile, VetProfile

# Register your models here.

admin.site.register(User, UserAdmin)

# Custom admin for Pet
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'is_featured', 'created_at')
    search_fields = ('name', 'species', 'breed')
    list_filter = ('species', 'is_featured')
    ordering = ('-created_at',)  # Newest first

admin.site.register(Pet, PetAdmin)
admin.site.register(ShelterProfile)
admin.site.register(VetProfile)