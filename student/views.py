from django.shortcuts import redirect, render
from .forms import UpdateProfileForm,UserProfileForm
from .models import Student
from django.core.exceptions import ObjectDoesNotExist
# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UpdateProfileForm(data=request.POST, instance=request.user)
#         update = form.save(commit=False)
#         update.user = request.user
#         update.save()
#     else:
#         form = UpdateProfileForm(instance=request.user)

#     return render(request, 'student_profile.html', {'form': form})


def student_profile(request):
    try:
        userprofile = request.user.userprofile
    except ObjectDoesNotExist:
        userprofile = Student(user=request.user)
        
    if request.method == 'POST':
        user_form = UpdateProfileForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile.user)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            #user.username = user.email
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('student-home')
    else:
        profile_form = UserProfileForm(instance=request.user.userprofile)
        user_form = UpdateProfileForm(instance=request.user)
    args = {
        'user_form': user_form, # basic user form
        'profile_form': profile_form # user profile form
        }
    return render(request, 'student_profile.html', args)

def student_home(request):
    return render(request,'student_home.html')

def redeem(request):
    return render(request,'redeem.html')