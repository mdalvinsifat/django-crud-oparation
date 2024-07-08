
from django.shortcuts import render
from posts.models import post
def add_home (request):
    data= post.objects.all()
    return render(request,'home.html', {'data':data})