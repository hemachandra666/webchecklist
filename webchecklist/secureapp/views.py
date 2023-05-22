from email import message
from django.shortcuts import redirect, render

from .forms import CreateUserForm

from django.contrib.auth.models import auth


from django.contrib.auth.decorators import login_required


from django.contrib import messages



# Create your views here.

def home(request):

    return render(request, 'index.html')


def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("two_factor:login")


    context = {'form': form}

    return render(request, 'register.html', context=context)



@login_required(login_url='two_factor:login')
def dashboard(request):

    return render(request, 'dashboard.html')



def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("")



def account_locked(request):

    return render(request, 'account-locked.html')















