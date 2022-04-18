import email
import profile
from unicodedata import name
from django.db import models
from django.dispatch import receiver
from djano.contrib.auth.models import User

# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_lenght=70)
    admin = models.ForeignKey("Profile",on_delete=models.CASCADE,related_name='hood')
    hood_logo =  models.ImageField(upload_to='static/static_dirs/images/')
    description = models.TextField()
    health_info = models.IntegerField(null=True,blank=True)
    health_officer = models.CharField(max_length=60, null=True,)
    police_info = models.IntegerField(null=True, blank=True)
    police_officer=models.CharField(max_length=60,null=True, blank=True)

    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neibourhood(self):
        self.delete()

    @classmethod
    def find_neibourhood(cls, neibourhood_id):
        return cls.objects.filter(id=neibourhood_id)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=254, blank=True)
    profile_picture=  models.ImageField(upload_to='static/static_dirs/images/')
    location = models.CharField(max_length=50, blank=True, null=True)
    NeighbourHood=models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL,null=True, related_name='members',blank=True)

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender,instance, created):
        Profile.objects.create(user=instance)
        if created:
            Profile.objects.create(user=instance)

            
    @receiver(post_save, sender=user)
    def save_user_profile(sender,instance,):
        instance.profile.save()

class Business(models.Model)
name=models.CharField(max_length=100)
email=models.EmailField(max_length=254)
description=models.TextField(blank=True)
neighbourhood=models.ForeignKey(NeighbourHood, on_delete=models.CASCADE,related_name="business")
user=models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='owner')

def __str__(self):
    return f'{self.name} Business'

def create_business(self):
    self.save()

def delete_business(self):
    self.delete()

@classmethod
def search_business(cls,name):
    return cls.objects.filter(name__icontains=name).all()

