from django.shortcuts import redirect, render

from trainer.models import Trainer
from .forms import TrainerUpdateProfileForm, TrainerUserProfileForm
from django.core.exceptions import ObjectDoesNotExist

def trainer_home(request):
    trainers=Trainer.objects.all()
    print(trainers)
    return render(request,'trainer.html')

def trainer_profile(request):
    try:
        traineruserprofile = request.user.traineruserprofile
    except ObjectDoesNotExist:
        traineruserprofile = Trainer(user=request.user)
        
    if request.method == 'POST':
        user_form = TrainerUpdateProfileForm(request.POST, instance=request.user)
        profile_form = TrainerUserProfileForm(request.POST, instance=request.user.traineruserprofile.user)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            #user.username = user.email
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('trainer-home')
    else:
        profile_form = TrainerUserProfileForm(instance=request.user.traineruserprofile)
        user_form = TrainerUpdateProfileForm(instance=request.user)
    args = {
        'user_form': user_form, # basic user form
        'profile_form': profile_form # user profile form
        }
    return render(request, 'trainer_profile.html', args)


