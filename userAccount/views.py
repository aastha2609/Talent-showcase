from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import Post,Profile
from django.contrib.auth.models import User


# Create your views here.
def userHome(request):
    posts=Post.objects.all().order_by('pk')
    data={'posts':posts}
    return render(request,'myaccount.html',data)


def post(request):
    if request.method =="POST":
        image=request.FILES['image']
        # image=request.POST.FILES.get('image','')
        # image=request.POST.get('image','')
        caption=request.POST.get('caption','')
        userId=request.user

        postObj=Post(caption=caption,image=image,userId=userId)
        postObj.save()
        print(caption)
        messages.success(request,"Posted Successfully ! ")
        return redirect('/userAccount')
    else:
        messages.error(request,"Something went wrong ")
        return redirect('/userAccount')

def userpost(request):
    return render(request,'userpost.html')

def delPost(request,PostId):
    post_fetch=Post.objects.filter(pk=PostId)
    # print(post_fetch)
    # image_path=post_fetch[0].image.url#image location
    post_fetch.delete()
    messages.info(request,'Your post has been removed')
    return redirect('/userAccount')



def userProfile(request,username):
    user=User.objects.filter(username=username)

    if user:
        user=user[0]
        profile=Profile.objects.get(user=user)
        post=getpost(user)
        bio=profile.bio
        conn=profile.connection
        follower=profile.follower
        following=profile.following
        user_img=profile.userImage

        data={'user_obj':user,
        'bio':bio,
        'conn':conn,
        'posts':post,
        'follower':follower,
        'following':following,
        'userImg':user_img}
        return render(request,'userProfile.html',data)

    else:
        return HttpResponse('no user')
    # return render(request,'userAccount/userProfile.html',data)

def getpost(user):
    # user=request.user
    post_obj=Post.objects.filter(userId=user)
    imgList=[post_obj[i:i+3] for i in range(0,len(post_obj),3)]
    return imgList
