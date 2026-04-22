from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Item
from .forms import ItemForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User

@login_required
def home(request):
    items = Item.objects.filter(owner=request.user).order_by('-id')
    category = request.GET.get('category')
    if category and category != 'All':
        items = items.filter(category=category)
    categories = Item.CATEGORY_CHOICES
    return render(request, 'core/home.html', {'items': items, 'categories': categories, 'selected': category})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('closet')
    else:
        form = ItemForm()
    return render(request, 'core/item_form.html', {'form': form, 'title': 'Add Item'})

@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('closet')
    else:
        form = ItemForm(instance=item)
    return render(request, 'core/item_form.html', {'form': form, 'title': 'Edit Item'})

@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk, owner=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('closet')
    return render(request, 'core/confirm_delete.html', {'item': item})

@login_required
def dashboard(request):
    total_spent = Item.objects.filter(owner=request.user).aggregate(Sum('purchase_price'))['purchase_price__sum'] or 0
    total_earned = Item.objects.filter(owner=request.user, status='Sold').aggregate(Sum('sold_price'))['sold_price__sum'] or 0
    items_sold = Item.objects.filter(owner=request.user, status='Sold').count()
    items_listed = Item.objects.filter(owner=request.user, status='Listed').count()
    items_keeping = Item.objects.filter(owner=request.user, status='Keeping').count()
    total_listing_value = Item.objects.filter(owner=request.user, status='Listed').aggregate(Sum('listing_price'))['listing_price__sum'] or 0
    most_expensive = Item.objects.filter(owner=request.user).order_by('-purchase_price').first()

    context = {
        'total_spent': total_spent,
        'total_earned': total_earned,
        'items_sold': items_sold,
        'items_listed': items_listed,
        'items_keeping': items_keeping,
        'total_listing_value': total_listing_value,
        'most_expensive': most_expensive,
    }
    return render(request, 'core/dashboard.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

def public_profile(request, username):
    from django.contrib.auth.models import User
    profile_user = get_object_or_404(User, username=username)
    items = Item.objects.filter(owner=profile_user, status='Listed').order_by('-id')
    categories = Item.CATEGORY_CHOICES
    category = request.GET.get('category')
    if category and category != 'All':
        items = items.filter(category=category)
    return render(request, 'core/public_profile.html', {
        'profile_user': profile_user,
        'items': items,
        'categories': categories,
        'selected': category,
    })

def browse(request):
    users = User.objects.filter(item__status='Listed').distinct()
    user_data = []
    for user in users:
        count = Item.objects.filter(owner=user, status='Listed').count()
        user_data.append({'user': user, 'count': count})
    return render(request, 'core/browse.html', {'user_data': user_data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.save()
        return redirect('home')
    return render(request, 'core/edit_profile.html')