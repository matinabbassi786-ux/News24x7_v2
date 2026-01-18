import re
from django.shortcuts import render
from django.contrib.auth.models import User
from Customer.models import Frend,UserInfo
from Journalist.models import JournalistInfo
from Articles.models import bookmarkArticle

def HomePage(request,user,id):
    try:
        userdb = User.objects.get(username=user,id=id)

        if userdb.id != request.user.id:
            Frendrequest = Frend.objects.create(user=request.user,frend=userdb)
            Frendrequest.save()
        
        Following = JournalistInfo.objects.filter(followers__id=userdb.id).count()
        Followers = JournalistInfo.objects.get(user=userdb.id)
        Bookmarks = bookmarkArticle.objects.all().filter(user=userdb).count()
       
        data = {
            'userdb': userdb,
            "Following":Following,
            "Followers":Followers.followers.count(),
            "Bookmarks":Bookmarks,
        }
        return render(request, 'index.html',data)          
    except User.DoesNotExist:
        return render(request, '404.html')
