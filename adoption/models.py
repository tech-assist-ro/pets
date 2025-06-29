from django.contrib.auth.models import AbstractUser
from django.db import models

# --- Custom User Model ---
class User(AbstractUser):
    USER_TYPES = [
        ('individual', 'Individual'),
        ('shelter', 'Shelter'),
        ('vet', 'Veterinarian'),
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='individual')

    def is_shelter(self):
        return self.user_type == 'shelter'

    def is_vet(self):
        return self.user_type == 'vet'

    def is_individual(self):
        return self.user_type == 'individual'
    

# --- Profiles ---
class ShelterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shelter_profile')
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    plan_type = models.CharField(max_length=50, choices=[
        ("free", "Free"),
        ("premium", "Premium")
    ], default="free")

    def __str__(self):
        return f"Shelter: {self.name}"
    

class VetProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vet_profile')
    clinic_name = models.CharField(max_length=255)
    license_id = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f"Vet: {self.clinic_name}"
    

# --- Pets ---
class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to="pets/")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.species})"
