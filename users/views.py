from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import token_generator

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home_page')
	else:
		form = UserRegisterForm()
		if request.method == 'POST':
			form = UserRegisterForm(request.POST)
			if form.is_valid():
				username = request.POST['username']
				email = request.POST['email']
				password = request.POST['password1']

				user = User.objects.create_user(username=username, email=email)
				print(password)
				user.set_password(password)
				user.is_active = False
				user.save()

				uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
				domain = get_current_site(request).domain
				link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token_generator.make_token(user)})

				activate_url = 'http://' + domain + link
				email_subject = 'Activate Your Account'
				email_body = 'Hi ' + user.username + 'Use link\n' + activate_url
				email = EmailMessage(
					email_subject,
					email_body,
					'thetriquetra01@gmail.com',
					[user.email],
				)
				email.send(fail_silently=False)

				messages.success(request, 'Account was created for ' + user.username)

				return redirect('login')

		context = {'form': form}
		return render(request, 'users/register.html', context)

class VerificationView(View):
	def get(self, request, uidb64, token):

		try:
			id = force_text(urlsafe_base64_decode(uidb64))
			user = User.objects.get(pk=id)

			if not token_generator.check_token(user, token):
				return redirect('login'+'?message='+'User already activated')

			if user.is_active:
				return redirect('login')
			user.is_active = True
			user.save()

			messages.success(request,'Account activated successfully')
			return redirect('login')
		except Exception as ex:
			pass


		return redirect('login')

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home_page')
	else:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			print(username, password)

			user = authenticate(request, username=username, password=password)
			print(user)
			if user:
				if user.is_active:
					login(request, user)
					return redirect('home_page')


			else:
				messages.info(request,
							  'Did you check your email to activate your account? If yes, then check credentials or else activate your account.')
		context = {}
		return render(request, 'users/login.html', context)

def logoutPage(request):
	logout(request)
	return redirect('home_page')

@login_required
def profile(request):
	return render(request, 'users/profile.html')

def profile_update(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'You account has been updated!')
			return redirect('profile')

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context = {
			'u_form': u_form,
			'p_form': p_form
	}

	return render(request, 'users/profile_update.html', context)