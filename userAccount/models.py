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
    userImage=models.ImageField(upload_to='media/Profiles',default='media/default/20A-1User-512.png')
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

class Following(models.Model):
    user_acc=models.OneToOneField(User,on_delete=models.CASCADE)
    followed=models.ManyToManyField(User,related_name='followed')

    @classmethod
    def follow(cls,user,another_account):
        obj,create=cls.objects.get_or_create(user=user_acc)
        obj.following.add(another_account)

    @classmethod
    def unfollow(cls,user,another_account):
            obj,create=cls.objects.get_or_create(user=user_acc)
            obj.following.remove(another_account)
