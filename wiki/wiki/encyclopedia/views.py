from django.shortcuts import render , redirect
import markdown
from . import util

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
        return render(request , "encyclopedia/index.html",{
            "message" : "The  entry input does not exist, here are some that do.",
            "entries" : util.list_entries()
        })

    else:
        return render(request , "encyclopedia/entrypage.html",{
            "content" : content , 
            "title" : title
        })


    


