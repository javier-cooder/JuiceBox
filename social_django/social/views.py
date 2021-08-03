
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.urls.base import reverse_lazy
from .models import*
from .forms import PasswordCha, PostForm, UserRegisterForm, ProfileForm
from .forms import  UserForm 
from .forms import PasswordCha
from django.contrib import messages 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.
def home(request):
    return render(request, 'social/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
    else: 
        form = UserRegisterForm()

    context = {'form' : form}
    return render(request, 'social/register.html', context)

@login_required
def feed(request):
    posts = Post.objects.all()
    context = { 'posts': posts}
    return render(request, 'social/feed.html', context)

@login_required
def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post publicado')
            return redirect('feed')
    else: 
        form = PostForm()
    return render(request, 'social/post.html', {'form' : form})

@login_required
def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all() 
        
    else: 
        posts = current_user.posts.all()
        user = current_user 
     
    return render(request, 'social/profile.html', {'user': user, 'posts':posts})

def password_succes(request):
    messages.success(request, 'Contraseña cambiada')
    return redirect('profile-update')
   
def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user)
    rel.save()
    messages.success(request, f'ahora sigues a {username}')
    return redirect('feed')

def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    messages.success(request, f'Ya no sigues a {username}')
    return redirect('feed')


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'social/edit_profile.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Tu informacion ha sido actualizada')
            return HttpResponseRedirect(reverse_lazy('profile-update'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class PasswordsChangeView(PasswordChangeView):
    form_class  = PasswordCha
    success_url=reverse_lazy('password_change_done')
