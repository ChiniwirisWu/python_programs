from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Departments

# Create your views here.

class indexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'departments'

    def get_queryset(self):
        return Departments.objects.all()

class detailView(generic.DetailView):
    template_name = 'detail.html'
    # model = model

def addNewPage(request):
    rq = request.POST
    dp = Departments(title=rq['title'], link=rq['link'], img=rq['img'], price=rq['price'], location=rq['location'])
    dp.save()
    return HttpResponseRedirect(reverse('tier_list:index'))
