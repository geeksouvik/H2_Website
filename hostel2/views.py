from django.views import generic
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,DetailView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.contrib.auth.models import User
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
        a_form = AlumniForm(request.POST, request.FILES)
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


def updates(request):
    context = {
      'posts': Post.objects.all()
    }
    return render(request, 'hostel2/update.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'hostel2/update.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


class UserPostListView(ListView):
    model = Post
    template_name = 'hostel2/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


