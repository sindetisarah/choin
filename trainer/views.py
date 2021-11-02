from django.shortcuts import render
from .forms import UpdateProfileForm

def trainer_dashboard(request):
    return render(request,'trainer.html')

def trainer_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(data=request.POST, instance=request.user)
        update = form.save(commit=False)
        update.user = request.user
        update.save()
    else:
        form = UpdateProfileForm(instance=request.user)

    return render(request, 'trainer_profile.html', {'form': form})