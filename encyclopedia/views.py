from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, title):
    if request.method == "GET":
        return render(request, "encyclopedia/entry_page.html", {
            "title": util.get_entry(title)
        })
    else:
        return render(request, "encyclopedia/error.html")


def create(request):
    return render(request, "encyclopedia/create.html")
