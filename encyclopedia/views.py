from random import choice
import random
from django.shortcuts import render, redirect
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
    headline = "Page not found"
    # Get value from form.
    if request.method == "POST":
        # Exceptions comes in different types, happens when the response is not true.
        try:
            return render(request, "encyclopedia/search_results.html", {
                "text": text.capitalize(),
                "search": search(request)
            })
        except TypeError:
            return render(request, "encyclopedia/error.html", {
                "headline": headline
            })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
        })


def entry_page(request, title):
    if request.method == "GET":
        return render(request, "encyclopedia/entry_page.html", {
            "title": markdowner.convert(util.get_entry(title)),
        })
    if request.method == "POST":
        see_title = title
        return edit_page(request, see_title)
    else:
        return render(request, "encyclopedia/error.html", {
            "headline": "Page not found",
        })


def create(request):
    # Set variables
    title = request.POST.get("title")
    content = request.POST.get("content")
    headline = "File already exists"
    if request.method == "POST":
        # If entry already exists with same title
        textC = title.capitalize()
        item_list = item_lists = util.list_entries()
        for item in item_lists:
            # If the input text (str) is in the item (str), return the item.
            if textC in item_list:
                return render(request, "encyclopedia/error.html", {
                    "headline": headline
                })
            else:
                # If there's something to post, takes that input and use it in util functions.
                save_page = util.save_entry(title, content)
                preview = entry_page(request, title)
                return render(request, "encyclopedia/entry_page.html", {
                    "title": markdowner.convert(util.get_entry(title))
                })
    else:
        return render(request, "encyclopedia/create.html")


def edit_page(request, title):
    content = util.get_entry(title)
    save = request.POST.get("save")
    if content == None:
        return render(request, "encyclopedia/error.html", {'headline': "Page Not Found"})
    # Set variables
    content = request.POST.get("content")
    if request.method == "POST":
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit_page.html", {
            "content": util.get_entry(title),
            # "save": util.edit_entry(title, new_content2)
        })
        new_content = request.POST.get("content")
        new_content2 = new_content
    if save:
        util.edit_entry(title, new_content2)
        # If there's something to post, takes that input and use it in util functions.
        return render(request, "encyclopedia/entry_page.html", {
            "title": markdowner.convert(util.get_entry(title))
        })
    else:
        return render(request, "encyclopedia/entry_page.html", {
            "title": markdowner.convert(util.get_entry(title))
        })
    # else:
    return render(request, "encyclopedia/entry_page.html", {
        "title": markdowner.convert(util.get_entry(title))
    })


def random_page(request):
    # Set variables
    entries = util.list_entries()
    random_choice = random.choice(entries)
    text = []
    # Append value from choice to use it in post request.
    text.append(random_choice)
    choice = text[0]

    if request.method == "GET":
        return render(request, "encyclopedia/random.html", {
            "title": markdowner.convert(util.get_entry(random_choice)),
        })
    if request.method == "POST":
        return edit_page(request, choice)
    else:
        return render(request, "encyclopedia/error.html", {
            "headline": "Page not found",
        })


def search(request):
    # Set variables
    text = request.POST.get("q")
    # Take the value from the input and capitalize it to match with the search on list
    textC = text.capitalize()
    # Store the list of file to iterate
    item_lists = util.list_entries()
    # With for in, check each item of the list
    for item in item_lists:
        # If the input text (str) is in the item (str), return the item.
        if textC in item:
            return item
