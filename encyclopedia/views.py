import random
from django.shortcuts import render
from django.views.generic import ListView
from django.template import RequestContext

from . import util
from markdown2 import Markdown
# Set variable to use in the instance.
markdowner = Markdown()


def index(request):
    # Set variables to post the value from form tag.
    text = request.POST.get("q")
    item_lists = util.list_entries()

    # Get value from form.
    if request.method == "POST":
        search(request)
        # Exceptions comes in different types, happens when the response is not true.
        try:
            return render(request, "encyclopedia/entry_page.html", {
                "title": markdowner.convert(util.get_entry(text))
            })
        except TypeError:
            return render(request, "encyclopedia/search_results.html", {
                "entries": util.list_entries(),
                "search": text.capitalize()
            })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
        })


def entry_page(request, title):
    if request.method == "GET":
        # Get content from markdown file
        content = util.get_entry(title)
        try:
            return render(request, "encyclopedia/entry_page.html", {
                "title": markdowner.convert(util.get_entry(title)),
                "content": content
            })
        except 404:
            return render(request, "encyclopedia/error.html")


def create(request):
    # Set variables
    title = request.POST.get("title")
    content = request.POST.get("content")

    if request.method == "POST":
        # If there's something to post, takes that input and use it in util functions.
        save_page = util.save_entry(title, content)
        preview = entry_page(request, title)
        return render(request, "encyclopedia/entry_page.html", {
            "title": markdowner.convert(util.get_entry(title))
        })
    else:
        return render(request, "encyclopedia/create.html")


def edit_page(request):
    # Set variables
    title = request.POST.get("title")
    print("Text -", title)

    return render(request, "encyclopedia/edit_page.html", {
        "content": util.get_entry(title)
    })


def random_page(request):
    # Set variables
    entries = util.list_entries()
    print("List -", entries)
    random_choice = random.choice(entries)
    print("random_choice", random_choice)

    return render(request, "encyclopedia/random.html", {
        "title": markdowner.convert(util.get_entry(random_choice))
    })


def search(request):
    # Set variables
    text = request.POST.get("q")
    textC = text.capitalize()
    print("Text -", textC)
    item_lists = util.list_entries()
    print("List -", item_lists)
    for item in item_lists:
        if textC in item:
            print("Item -", item)
