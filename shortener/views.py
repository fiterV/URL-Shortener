from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import KirrURL
from django.views import View
from .forms import SubmitUrlForm

import socket

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
            #for proper redirect on a hosting
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
            #Well I decided that there won't be "exists" page
            #Let user think that he/she provided unique link
            #that we haven't in our DB before
            # if created==True:
            #     template="shortener/success.html"
            # else:
            #     template="shortener/already-exists.html"
        else:
            #Wrong link, error page
            context['failed']=True;
        print(context)

        return render(request, "shortener/success.html", context)


class KirrCBView(View):
    def get(self, request, code=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=code)
        return redirect(obj.url)