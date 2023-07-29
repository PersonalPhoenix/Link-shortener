import uuid

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Link


def home_page(request) -> HttpResponse:
    return render(request, 'based.html')

def create_uuid(request) -> HttpResponse:

    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:6]
        new_url = Link(url = url, uuid = uid)
        new_url.save()
        return HttpResponse(uid)
        
def redirect_by_shortened_url(request, pk) -> redirect:

    url_detail = Link.objects.get(uuid = pk)
    return redirect(url_detail.url)