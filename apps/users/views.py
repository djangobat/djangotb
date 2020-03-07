from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import CustomUserUpdateForm


@login_required
def profile(request):
    is_valid = None
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            is_valid = True
        else:
            is_valid = False
    else:
        form = CustomUserUpdateForm(instance=request.user)

    context = {
        'form': form,
        'is_valid': is_valid,
    }
    return render(request, 'users/profile.html', context)