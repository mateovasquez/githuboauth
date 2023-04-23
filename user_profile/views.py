from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from user_profile.forms import ProfileCreateUpdateForm, UserInfoForm

# Create your views here.

@login_required
def user_detail_view(request):
  if request.method == 'POST':
    user_form = UserInfoForm(request.POST, instance=request.user)
    return save_user_info(request, user_form)
  else:
    user_form = UserInfoForm(instance=request.user)
  return render(request, 'user-detail.html', {
    'user_form': user_form,
  })

def save_user_info(request, user_form):
  if user_form.is_valid():
    user_form.save()
    messages.success(request, ('Your user was successfully updated!'))
    return redirect('home')
  else:
    messages.error(request, ('Please correct the error below.'))


@login_required
def profile_detail_view(request):
  profile = getattr(request.user, "profile", None)
  return render(request, 'profile-detail.html', {
    'profile': profile,
  })


@login_required
def profile_edit_view(request):
  profile = getattr(request.user, "profile", None)
  if request.method == 'POST':
    return create_update_profile(request, profile)
  else:
    return show_profile(request, profile)
  

def show_profile(request, profile=None):
  form = ProfileCreateUpdateForm(instance=profile)
  context = {'form': form}
  return render(request, "profile-edit.html", context)


def create_update_profile(request, profile=None):
  form = ProfileCreateUpdateForm(request.POST, instance=profile)
  if form.is_valid():
    if not profile:
      form.instance.user = request.user
    form.save()
    messages.success(request, ('Your profile was successfully updated!'))
    return redirect('profile_detail')
  else:
    messages.error(request, ('Please correct the error below.'))
    context = {'form': form}
    return render(request, "profile-edit.html", context)
  
def profile_delete_view(request):
  profile = getattr(request.user, "profile", None)
  if request.method == 'POST':
    profile.delete()
    messages.success(request, ('Your profile was successfully deleted!'))
    return redirect('profile_detail')
  else:
    context = {'profile': profile}
    return render(request, "profile-delete.html", context)