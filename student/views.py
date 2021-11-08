from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import UpdateProfileForm,UserProfileForm
from .models import  *
from django.core.exceptions import ObjectDoesNotExist
from leadership.models import RedeemableItem, Transaction, Wallet


# @login_required



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
    reward_items=RedeemableItem.objects.all()
    bal = Wallet.objects.all().filter(owner = request.user)
    return render(request,'redeem.html',{'reward_items':reward_items,'bal':bal})

def redeem_failed(request):
    return render(request,'RedeemFailed.html')

def redeem_success(request):
    return render(request,'RedeemSucceed.html')

def redeem_active(request):
    return render(request,'redeem_active.html')

def student_transactions(request):
    transactions = Transaction.objects.all().filter(receiver = request.user.username)
    bal = Wallet.objects.all().filter(owner = request.user)
    return render(request,'student_transactions.html',{'transactions':transactions,'bal':bal})  

def view_redeemed_items(request):
    if request.user.is_authenticated:
        customer=request.user.idt
        order,created=Order.objects.get_or_create(customer=customer,completed=False)
        items=order.orderedproduct_set.all()
    else:
        items=[]

    context={"items":items,
            "order":order
    }
    # return render(request,'cart.html',context)
    return render(request,'view_redeemed_items.html',context)       


def mark_as_read(request,pk):
    
    notifications = Notifications.objects.get(pk=pk)
    notifications.mark_as_read()
    return redirect(reverse('student-home'))