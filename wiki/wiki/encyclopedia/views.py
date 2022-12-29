from django.shortcuts import render 
import markdown
from . import util
import random

def conversion(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    
    else:
        return markdowner.convert(content)



def index(request):
    
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entrypage(request , title):
    content = conversion(title)

    if content == None:
        return render(request , "encyclopedia/error.html",{
            "message" : "The  entry input does not exist, here are some that do.",
            "entries" : util.list_entries()
        })

    else:
        return render(request , "encyclopedia/entrypage.html",{
            "content" : content , 
            "title" : title
        })

def search(request):
    if request.method == "POST":
        search = request.POST["q"]

        #Convert the input into html
        content = conversion(search)

        #Check whether the entry exists in the encyclopedia
        if content is not None:
            return render(request , "encyclopedia/entrypage.html",{
                "content" : content , 
                "title" : search
        })

        else:
            #Get all the encyclopedia entries present in the storage.
            entries = util.list_entries()
            recommendation = []
            #Go through each and every entry checking.
            for entry in entries:
                if search.lower() in entry.lower():
                    recommendation.append(entry)

            return render(request , "encyclopedia/search.html",{
                "recommendation" : recommendation 
            })


        

def new(request):
    if request.method == "GET":
        return render(request , "encyclopedia/new.html")

    else:
        title = request.POST["title"]
        content = request.POST["content"]
        exist = util.get_entry(title)
        if exist is not None:
            return render(request , "encyclopedia/error.html",{
                "message" : "The entry you are trying to create already exists"
            })
        
        else:
            util.save_entry(title , content)
            htmlcontent = conversion(title)
            return render(request , "encyclopedia/entrypage.html",{
                "title" : title , 
                "content" : htmlcontent
            })


def edit(request):
    if request.method == "POST":
        title = request.POST["entry"]
        content = util.get_entry(title)
        return render(request , "encyclopedia/edit.html", {
            "title" : title ,
            "content" : content
        })

def save(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title , content)
        htmlcontent = conversion(title)
        return render(request , "encyclopedia/entrypage.html",{
            "title" : title , 
            "content" : htmlcontent
        })


def random_choice(request):
    entries = util.list_entries()
    randomchoice = random.choice(entries)
    content = conversion(randomchoice)
    return render(request , "encyclopedia/entrypage.html", {
        "title" : randomchoice , 
        "content" : content

    })

  





    


