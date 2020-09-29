from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    userId=models.ForeignKey(User,on_delete=models.CASCADE)
    caption=models.CharField(max_length=500)
    image=models.FileField(upload_to='media',blank=True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.userId)


class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    userImage=models.ImageField(upload_to='media/Profiles')
    bio=models.CharField(max_length=100)
    connection=models.URLField(blank=True)
    follower=models.IntegerField(default=0)
    following=models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)

class Like(models.Model):
    user = models.ManyToManyField(User, related_name="likingUser")
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    # likers = models.IntegerField(default = 0)

    @classmethod 
    def liked(cls, post, liking_user):
        obj, create = cls.objects.get_or_create(post= post)
        obj.user.add(liking_user)

    @classmethod 
    def disliked(cls, post, disliking_user):
        obj, create = cls.objects.get_or_create(post= post)
        obj.user.remove(disliking_user)

    def __str__(self):
        return str(self.post)