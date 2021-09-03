from django.shortcuts import render, redirect
from .models import Items
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import AddItemForm
from django.db.models import Q

# Create your views here.

# require login to view or create your items
@login_required(login_url='signin')
def itemlist(request):
    '''
    creates function for showing all items related to specific user
    '''
    #getting all data/objects from logged in user
    users = request.user.items.all()

    #return item list on homepage after log in
    return render(request, "index.html", {'users': users})


# require login to view or create your items
@login_required(login_url='signin')
def additem(request):
    '''
    create a view function for adding new items to user list
    '''
    # checking request is post or not
    if request.method == 'POST':
        # item addition form
        form = AddItemForm(request.POST)
        # if form is valid means data is ok then save item
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            #using great django messages
            messages.success(request, 'YOur item addition success')
            return redirect('itemlist')

    else:
        form = AddItemForm()
        return render(request, 'add.html', {'form': form})

# require login to view or create your items
@login_required(login_url='signin')
def updateitem(request, pk):
    '''
    creates a view function for updating existing items
    '''
    user = Items.objects.get(id=pk)
    if request.method == 'POST':
        form = AddItemForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated succesfully')
            return redirect('itemlist')
    else:
        form = AddItemForm(instance=user)
        return render(request, 'update.html', {'form': form})

# require login to view or create your items
@login_required(login_url='signin')
def deleteitem(request, pk):
    '''
    view function for deleting existing items
    '''
    user = Items.objects.get(id=pk)
    #using query delete function to delete item
    user.delete()
    messages.success(request, 'Succesfully deleted item!')
    return redirect('itemlist')

# require login to view or create your items
@login_required(login_url='signin')
def filteritem(request):
    '''
    view finction for filtering items according to date
    '''
    if request.method == 'GET':

        query = request.GET.get('query')
        #using filter function
        filter = Items.objects.filter(Q(date__icontains=query))
        return render(request, 'filter.html', {'query': query, 'filter': filter})
    else:
        return render(request, 'index.html')


def signup(request):
    '''
    this view function is for making sign up backend logic with all the validations and fields
    '''

    # checking request is for post or not
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. Click login button to login")
            return redirect('signup')
        else:
            messages.error(request, "Registration unsuccesful.")
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def signin(request):
    '''
    view function logic for signing in user
    '''
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('itemlist')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def signout(request):
    '''
    view function logic for signing out
    '''
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('signin')






