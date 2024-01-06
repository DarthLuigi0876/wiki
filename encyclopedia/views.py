from django.shortcuts import render, redirect
import re
import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    content = markdown.markdown(content)
    if not content:
        content = "Page not found (404)"
    return render(request, "encyclopedia/entry.html",{
        "title":title, "content":content
    })

def search(request):
    entries=[]
    q = request.GET.get('q')
    if q in util.list_entries():
        return redirect("entry", title=q)
    for entry in util.list_entries():
        if re.search(q.lower(), entry.lower()):
            entries.append(entry)
    return render(request, "encyclopedia/search.html",{
        'q':q, 'entries':entries
    })