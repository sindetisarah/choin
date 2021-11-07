from django.shortcuts import redirect, render
from .forms import UpdateProfileForm,UserProfileForm
from .models import Redeem, RewardedItem, Student
from django.core.exceptions import ObjectDoesNotExist
from leadership.models import RedeemableItem, Transaction, Wallet
from django.http import JsonResponse
import json
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
    if request.user.is_authenticated:
        student_customer = request.user.role == 3
        order, created = Redeem.objects.get_or_create(student=student_customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.calculate_cart_items
    else:
        items= []
    reward_items=RedeemableItem.objects.all()
    
    bal = Wallet.objects.all().filter(owner = request.user)
    return render(request,'redeem.html',{'reward_items':reward_items,'bal':bal, 'cartItems':cartItems })
def redeem_failed(request):
    return render(request,'RedeemFailed.html')
def redeem_success(request):
    if request.user.is_authenticated:
        student_customer = request.user.role==3
        order, created = Redeem.objects.get_or_create(student=student_customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items= []
    context = {'items':items, 'order':order}  
    return render(request,'RedeemSucceed.html')
def cart(request):
    if request.user.is_authenticated:
        student_customer = request.user.role == 3
        order, created = Redeem.objects.get_or_create(student=student_customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items= []

    context = {'items':items, 'order':order}    
    return render(request,'cart.html', context)

def student_transactions(request):
    transactions = Transaction.objects.all().filter(receiver = request.user.username)
    bal = Wallet.objects.all().filter(owner = request.user)
    
    

    return render(request,'student_transactions.html',{'transactions':transactions,'bal':bal})  

def update_item(request):
    data = json.loads(request.data)
    productId = data['productId'] 
    action = data['action']

    print('Action:', action)
    print('ProductId:', productId) 

    student_customer = request.user.role ==3
    product = RedeemableItem.objects.get(id=productId)
    order, created = Redeem.objects.get_or_create(student=student_customer, complete = False)
    orderItem, created = RewardedItem.objects.get_or_create(order = order, product=product)

    if action =='add':
        orderItem.quantity = (orderItem.quantity +1)
    elif action == 'remove':
         orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
