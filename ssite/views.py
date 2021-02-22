from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

#Importing all models
# from .models import 



class Blog(TemplateView):

    def get(self, *args, **kwargs):

        return render(
        request = self.request,
        template_name = 'blog.html',
        context = {

        }
        )
