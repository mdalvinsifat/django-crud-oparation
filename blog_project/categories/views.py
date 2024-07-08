from django.shortcuts import render, redirect
from . import forms
# Create your views here.
def add_category(request):
    if request.method== "POST":
        author_form = forms.Add_category(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('add_author')
    else :
         author_form = forms.Add_category()
         
    return render(request, 'add_author.html', {"form":author_form})


