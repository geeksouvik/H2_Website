from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import *
from .forms import AlumniForm

def base(request):
    return render(request, 'hostel2/landingpage.html')



def home(request):
    updates = Updates.objects.all()
    context = {'updates':updates}
    return render(request, 'hostel2/homenew.html',context)

def gallery(request):
    return render(request, 'hostel2/gallery.html')

def alumni(request):
    a_form = AlumniForm()
    if request.method == 'POST':
        a_form = AlumniForm(request.POST)
        if a_form.is_valid():
            a_form.save()
            messages.success(request, f'You testimony has been submitted!')

    return render(request, 'hostel2/alumni.html',{ 'a_form' : a_form})





def legend(request):
    all_categorys = Legend_Category.objects.all()
    all_legends = Legends.objects.order_by("-year")
    context = { 'all_categorys' : all_categorys, 'all_legends' : all_legends}
    return render(request, 'hostel2/legend.html', context)

def contactus(request):
    ##all_council_categorys = Council_Category.objects.all()
    ##all_council = Council.objects.all()
    ##context = { 'all_council_categorys' : all_council_categorys, 'all_council' : all_council}
    admin_council = AdminCouncil.objects.all()
    web_council = WebCouncil.objects.all()
    maint_council = MaintCouncil.objects.all()
    mess_council = MessCouncil.objects.all()
    tech_council = TechCouncil.objects.all()
    cult_council = CultCouncil.objects.all()
    events_council = EventsCouncil.objects.all()
    sports_council = SportsCouncil.objects.all()
    context = { 'admin_council' : admin_council, 'web_council' : web_council, 'maint_council':maint_council,'mess_council':mess_council ,'tech_council':tech_council, 'cult_council':cult_council,'events_council':events_council,'sports_council':sports_council }
    return render(request, 'hostel2/contactus_test.html', context)