from django.shortcuts import render
from . import util
from markdown2 import Markdown
import random



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def html_convertor(title):
    title_exists = util.get_entry(title)
    if title_exists == None:
        return None
    else:
        markdowner = Markdown()
        return  markdowner.convert(title_exists)

def entry(request,name):
    title_content = html_convertor(name)
    if title_content == None:
        return render(request,"encyclopedia/error.html",{
            "message": f"Page for {name} Doesnt Exist"
        })
    else:
        return render(request,"encyclopedia/entry.html",{
            "title":name,
            "content":title_content
        })

def search(request):
    if request.method == "POST":
        title = request.POST['q']
        title_content = html_convertor(title)
        if title_content is not None:
            return render(request,"encyclopedia/entry.html",{
                "title":title,
                "content":title_content
            })
        else:
            str_match = []
            list_entries = util.list_entries()
            for entry in list_entries:
                if title.lower() in entry.lower():
                    str_match.append(entry)
                    return render(request,"encyclopedia/search.html",{
                        "entries":str_match
                    })

def new_page(request):
    if request.method == "GET":
        return render(request,"encyclopedia/new_page.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        title_exists = util.get_entry(title)
        if title_exists is not None:
            return render(request,"encyclopedia/error.html",{
                "message":f"Page with title:{title} already exists"
            })
        else:
            util.save_entry(title,content)
            title_content = html_convertor(title)
            return render(request,"encyclopedia/entry.html",{
                "title":title,
                "content":title_content
            })

def edit_content(request):
    if request.method == "POST":
        title = request.POST['title']
        title_content = util.get_entry(title)
        return render(request,"encyclopedia/edit_page.html",{
            "title":title,
            "content":title_content
        }) 

def edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title,content)
        title_content = html_convertor(title)
        return render(request,"encyclopedia/entry.html",{
            "title":title,
            "content":title_content
        })

def randomizer(request):
    entry_list = util.list_entries()
    rand_title = random.choice(entry_list)
    title_content = html_convertor(rand_title)
    return render(request,"encyclopedia/entry.html",{
        "title":rand_title,
        "content":title_content
    })
