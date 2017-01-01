from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import KirrURL
from django.views import View
from .forms import SubmitUrlForm

import socket

# Create your views here.
# def index(request, code):
#     obj = get_object_or_404(KirrURL, shortcode=code)
#     return redirect(obj.url)
#     return HttpResponse("Hey buddy " + obj.url)

class HomeView(View):
    def get(self, request, *args, **kwargs):
        tform = SubmitUrlForm()
        context = {
            'form':tform,
        }
        return render(request, "shortener/home.html", context)
    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        template="shortener/home.html"
        context = {
            "form": form,
            'host': request.get_host(),
        }
        if form.is_valid():
            print(form.cleaned_data)
            url = form.cleaned_data.get('url')
            obj, created = KirrURL.objects.get_or_create(url=url)
            context = {
                'object':obj,
                'created':created,
                'host':request.get_host(),
            }
            # if created==True:
            #     template="shortener/success.html"
            # else:
            #     template="shortener/already-exists.html"
        else:
            context['failed']=True;
        print(context)

        return render(request, "shortener/success.html", context)


class KirrCBView(View):
    def get(self, request, code=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=code)
        return redirect(obj.url)