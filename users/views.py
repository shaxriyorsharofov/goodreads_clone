from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from users.forms import UserCreateForm, UserUpdateForm


# Create your views here.


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            'form': create_form,
        }
        return render(request, 'users/register.html', context)


    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():

            create_form.save()

            # username = request.POST['username']
            # first_name = request.POST['first_name']
            # last_name = request.POST['last_name']
            # email = request.POST['email']
            # password = request.POST['password']
            #
            # user = User.objects.create(
            #     username=username,
            #     first_name=first_name,
            #     last_name=last_name,
            #     email=email
            # )
            # user.set_password(password)
            # user.save()

            return redirect('users:login')
        else:
            context = {
                'form': create_form,
            }
            return render(request, 'users/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        messages.success(request, "Siz muvaffaqqiyatli saytga kirdingiz!")
        return render(request, 'users/login.html', {'login_form': login_form})


    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('landing_page')
        else:
            return render(request, 'users/login.html', {'login_form': login_form} )



class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Siz saytdan chiqib ketdinggiz!")
        return render(request, 'landing_page.html')


class UserProfileView(View):
    def get(self, request):
        return render(request, 'users/user_profile.html', {'user': request.user})


class UserUpdateView(View):
    def get(self, request):
        user_update_view = UserUpdateForm(instance=request.user)

        return render(request, 'users/update_profile.html', {"form": user_update_view})
    def post(self, request):
        user_update_view = UserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
                                          )
        if user_update_view.is_valid():
            user_update_view.save()

            return render(request, 'users/user_profile.html')

        return render(request, 'users/update_profile.html', {"form": user_update_view})




