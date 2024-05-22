from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import util

from markdown2 import Markdowns
import random


def index(request):
    entries = util.list_entries()
    return render(request, 'encyclopedia/index.html', {'entries': entries})


def entry_detail(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, 'encyclopedia/error.html', {'message': f'Page "{title}" does not exist.'}, status=404)
    return render(request, 'encyclopedia/entry_detail.html', {'title': title, 'content': content})


def create_new_entry(request):
    markdowner = Markdown()
    if request.method == 'POST':
        title = request.POST['title']
        content = markdowner.convert(request.POST['content'])
        entries = util.list_entries()
        if title in entries:
            return render(request, 'encyclopedia/error_2.html')
        else:

            util.save_entry(title, content)
            return HttpResponseRedirect(f'/wiki/{title}/')
    else:
        return render(request, 'encyclopedia/create_new_entry.html')


def edit_entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, 'encyclopedia/error.html', {'message': f'Page "{title}" does not exist.'}, status=404)

    markdowner = Markdown()

    if request.method == 'POST':
        content = markdowner.convert(request.POST['content'])
        util.save_entry(title, content)
        return HttpResponseRedirect(f'/wiki/{title}/')
    else:
        return render(request, 'encyclopedia/edit.html', {'title': title, 'content': content})

def search(request):
    query = request.GET.get('q')
    entries = util.list_entries()
    results = []

    for entry in entries:
        if query.lower() in entry.lower():
            results.append(entry)

    if results:
        return render(request, 'encyclopedia/search.html', {'results': results})
    else:
        return render(request, 'encyclopedia/error.html')
def random_page(request):
    entries = util.list_entries()

    if entries:
        random_len = random.randint(0, len(entries) - 1)
        title = entries[random_len]
        content = util.get_entry(title)

        return render(request, 'encyclopedia/entry_detail.html', {'title': title, 'content': content})
    else:
        return render(request, 'encyclopedia/error.html')
