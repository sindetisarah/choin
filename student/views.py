from django.shortcuts import render
from .forms import UpdateProfileForm

# @login_required
def profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(data=request.POST, instance=request.user)
        update = form.save(commit=False)
        update.user = request.user
        update.save()
    else:
        form = UpdateProfileForm(instance=request.user)

    return render(request, 'student_profile.html', {'form': form})


def redeem(request):
    return render(request,'redeem.html')