from django.shortcuts import reverse, redirect, render
from user.forms.registration_form import ProfileForm, UserForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        profile_form = ProfileForm(data=request.POST, files=request.FILES)
        user_form = UserForm(data=request.POST)
        if profile_form.is_valid() and user_form.is_valid():
            # Saving to the database
            prof = profile_form.save(commit=False)
            prof.profileImage = (prof.profileImage if prof.profileImage else 'profileImages/user.png')
            prof.user = user_form.save()
            new_user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('profile')
        else:
            # The user reenters invalid information
            context = {'profile_form': profile_form, 'user_form': user_form}
            return render(request, 'user/register.html', context)
    else:
        # The page is initially loaded with blank a form.
        context = {'profile_form': ProfileForm(), 'user_form': UserForm()}
        return render(request, 'user/register.html', context)

def profile(request):
    return render(request, 'user/profile.html')