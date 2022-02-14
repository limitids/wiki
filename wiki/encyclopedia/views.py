from django.shortcuts import render,redirect
import markdown2
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
import random

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