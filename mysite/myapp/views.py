from audioop import add
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from myapp import models
from .models import Link
from django.http import HttpResponseRedirect
# Create your views here.
def scrape(request):
    if request.method == 'POST':
        site = request.POST.get('site', '')
    
    
        page = requests.get('https://unsplash.com/s/photos/dog')
        soup = BeautifulSoup(page.text,'html.parser')
    
    #link_address = []
     # create a list of links and append links into it
    
        for link in soup.find_all('a'):
        # link_address.append(link.get('href'))
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)
            
        return HttpResponseRedirect("/")
    else:
        data = Link.objects.all()
           
    return render(request, 'myapp/result.html', {'data': data})

def delete(request):
    Link.objects.all().delete()
    return render(request, 'myapp/result.html')