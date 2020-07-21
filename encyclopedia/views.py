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
    # Set variables.
    text = request.POST.get("q")
    # Get value from form.
    if request.method == "POST":
        return render(request, "encyclopedia/entry_page.html", {
            "title": markdowner.convert(util.get_entry(text))
        })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
        })


def entry_page(request, title):
    if request.method == "GET":
        return render(request, "encyclopedia/entry_page.html", {
            "title": markdowner.convert(util.get_entry(title))
        })
    else:
        return render(request, "encyclopedia/error.html")


def create(request):
    return render(request, "encyclopedia/create.html")
