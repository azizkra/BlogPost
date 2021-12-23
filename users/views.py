from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForms, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(requset):
    if requset.method == "POST":
        form = UserRegisterForms(requset.POST)  # if form post = need to create new form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                requset, f"Your Account has Been Created! You are Now Able to Log in"
        )
            return redirect("login")
    else:
        form = UserRegisterForms()
    return render(requset, "users/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account Has Been Updated!')
            return redirect('profile')
            
    else:
        u_form = UserUpdateForm(instance=request.user)  
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context ={
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'users/profile.html', context)