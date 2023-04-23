from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from user_profile.forms import UserInfoForm

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
    messages.success(request, ('Your profile was successfully updated!'))
    return redirect('home')
  else:
    messages.error(request, ('Please correct the error below.'))