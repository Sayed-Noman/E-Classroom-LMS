from django.shortcuts import render
from django.http import HttpResponse
from users.forms import UserProfileInfoForm,UserForm

def index(request):
    return HttpResponse('This is Homepage')


def register(request):
    registered  = False

    if register.methode == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data= request.POST)

        if user_form.is_valid() and profile_form.is_valid() :
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit= False)
            profile.user = user
            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form =UserForm()
        profile_form = UserProfileInfoForm()
    

    context ={
        'registered': registered,
        'user_form': user_form,
        'profile_form': profile_form,
    }
    
    return render(request, 'users/registration.html', context)