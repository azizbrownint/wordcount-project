from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordfukker = fulltext.split()

    worddictionary = {}

    for word in wordfukker:
        if word in worddictionary:
        #increase
            worddictionary[word] += 1

        else:
        #add to worddictionary
            worddictionary[word] = 1

        sortedwordlist = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordfukker), 'worddictionary':sortedwordlist})
