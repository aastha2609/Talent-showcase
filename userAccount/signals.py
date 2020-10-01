from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf.auth.models import User
from userAccount.models import Profile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    Profile.objects.create(user=instance)
    print('profile created succesfully')
