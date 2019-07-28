from django.db.models.signals import post_save                  #signal used when user is created
from django.contrib.auth.models import User                     #imports the 'User' model, it is the sender as it sends the signal
from django.dispatch import receiver                            #recieves the signal from the 'User' model
from .models import Profile                                     #creates the model

@receiver(post_save, sender=User)                               #when a user is created, it sends a signal that is recieved and runs the following code
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)                               #used to save the instance created in the previous function
def save_profile(sender, instance, **kwargs):
    instance.profile.save()