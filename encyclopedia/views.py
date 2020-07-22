from django.shortcuts import render
from django.views.generic import ListView
from django.template import RequestContext

from . import util
from markdown2 import Markdown
# Set variable to use in the instance.
markdowner = Markdown()
# markdowner.convert("*boo!*")
# u'<p><em>boo!</em></p>\n'
# markdowner.convert("**boom!**")
# u'<p><strong>boom!</strong></p>\n'


def index(request):
    # Set variables to post the value from form tag.
    text = request.POST.get("q")
    item_lists = util.list_entries()

    # Get value from form.
    if request.method == "POST":
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
        try:
            return render(request, "encyclopedia/entry_page.html", {
                "title": markdowner.convert(util.get_entry(title))
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
    initial = util.get_entry(title)
    return render(request, "encyclopedia/edit_page.html", {
        "content": initial
    })


def random(request):
    # Set variables
    entries = util.list_entries()
    print("entries")
    val = random.random
    return render(request, "encyclopedia/entry_page.html", {
        "random": markdowner.convert(util.get_entry(val))
    })
