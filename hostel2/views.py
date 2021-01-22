from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render,redirect,get_object_or_404
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
    testimony = Testimony.objects.all()
    a_form = AlumniForm()
    if request.method == 'POST':
        a_form = AlumniForm(request.POST)
        if a_form.is_valid():
            a_form.save()
            messages.success(request, f'You testimony has been submitted!')
    context = {'testimony': testimony}

    return render(request, 'hostel2/alumni.html',{ 'a_form' : a_form},context)

def legend(request):
    all_categorys = Legend_Category.objects.all()
    all_legends = Legends.objects.order_by("-year")
    context = { 'all_categorys' : all_categorys, 'all_legends' : all_legends}
    return render(request, 'hostel2/legend.html', context)

def contactus(request):
    all_council_categories = Council_Category.objects.all().order_by("-order")
    all_council = Council.objects.all()
    context = { 'all_council_categories' : all_council_categories,'all_council' : all_council}
    return render(request, 'hostel2/contactus_test.html', context)


############## contracts and documents ################

def info(request):
    return render(request, 'hostel2/info.html' )

############ Blog ####################

def blog(request):
    context = {
      'posts': Post.objects.all()
    }
    return render(request, 'hostel2/blog.html', context)

class PostListView(ListView):
  model = Post
  template_name = 'hostel2/blog.html'
  context_object_name = 'posts'
  ordering = ['-date_posted']
  paginate_by = 3

class UserPostListView(ListView):
  model = Post
  template_name = 'hostel2/blog.html'
  context_object_name = 'posts'
  paginate_by = 3

  def get_queryset(self):
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
  model = Post
  
class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['title','content'] 

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  fields = ['title','content'] 

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

def error_404_view(request,exception):
    return render(request, '404.html')