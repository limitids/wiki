from email import contentmanager
from logging import PlaceHolder
from django.shortcuts import render,redirect
import markdown2
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
import random

class createEntry(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget = forms.Textarea())

class editEntry(forms.Form):
        title = forms.CharField()
        content = forms.CharField(widget = forms.Textarea())



def index(request):
    if request.GET.get('q','') != '':
        return HttpResponseRedirect('wiki/'+(request.GET.get('q','')))

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def entry(request,file):

    if util.get_entry(file) == None:
        return render(request,'encyclopedia/notfound.html')
    
    return render(request,"encyclopedia/entry.html",{
        "entry": markdown2.markdown(util.get_entry(file)),
        "title":file
    })

def rando(request):
    listEntries = util.list_entries()
    Entry = listEntries[random.randint(0,len(listEntries)-1)]

    return redirect('entry',Entry)


def edit(request,file):
    if request.method == 'POST':
        util.save_entry(file,request.POST.get('edit',''))
        return redirect('entry',file)

    return render(request,"encyclopedia/edit.html",{
        "entry": markdown2.markdown(util.get_entry(file)),
        "title":file,
    })



def createPage(request):

    if request.method == "POST":
        form = createEntry(request.POST)
        if form.is_valid(): #server side checking of form
            title = form.cleaned_data["title"]
            md = form.cleaned_data["content"]
            entries = util.list_entries()
            for i in entries:
                if i == title:
                    return render(request,"encyclopedia/create.html", {
                        "form": createEntry(),
                        "error": 'Article already exists'
                    })

            util.save_entry(title,md)
            return redirect('entry',title)
            


    return render(request,"encyclopedia/create.html", {
        "form": createEntry(),
        "error": ''
    })