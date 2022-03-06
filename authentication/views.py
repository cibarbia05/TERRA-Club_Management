import os

import django
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

import management.views

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

# from authentication.excel_util import simple_upload
from authentication.forms import RegistrationForm, SignInForm, PasswordForgotEmail, SetPasswordForm
from authentication.models import User, TitleImage
from authentication.user_utility import is_club_sponsor


def main_page(request):
    title_images = TitleImage.objects.all()
    if request.user.is_authenticated:
        print(is_club_sponsor(request.user))
        return redirect('dashboard')
        # return redirect(reverse('dashboard', args=(is_sponsor(request.user),)))


    else:
        return render(request, 'authentication/main_page.html', {
            "title_images": title_images,

        })


def authentication_actions(request):
    return render(request, 'authentication/authentication_actions.html', {

    })


def register_info(request):
    return render(request, 'authentication/register_info.html', {
    })


def register(request):
    if request.method == 'GET':
        registration_form = RegistrationForm()

        return render(request, 'authentication/register.html', {
            'registration_form': registration_form
        })

    else:
        registration_form = RegistrationForm(request.POST)
        print(registration_form.errors)
        if registration_form.is_valid():
            email = str(registration_form.data['email'])
            return HttpResponseRedirect(reverse('set_account_password_email', args=(email,)))

        return redirect("register")


def sign_in(request):
    if request.method == "GET":
        sign_in_form = SignInForm()
        return render(request, 'authentication/signin.html', {
            'sign_in_form': sign_in_form
        })

    else:
        sign_in_form = SignInForm(request.POST)
        if sign_in_form.is_valid():
            print(sign_in_form.data['id'])
            print(sign_in_form.data['password'])

            user = User.objects.get(school_id=sign_in_form.data['id'])
            print(user.password)
            # user = authenticate(id=sign_in_form.data['id'], password=sign_in_form.data['password'])
            is_valid_password = user.check_password(sign_in_form.data['password'])
            if is_valid_password:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')


                return redirect('dashboard')
            # return redirect(reverse('dashboard', args=(is_sponsor(request.user),)))
            else:
                return render(request, 'authentication/error.html', {
                    'error_message': "Invalid Credentials",

                })
            # management.views.dashboard(request)


def set_account_password_email(request, email):
    user = User.objects.filter(email=email)
    if user.exists():
        user_u = User.objects.get(email=email)
        if user_u.password is None:
            entered_email = user_u.email

            for u in user:
                system_mail_email = os.environ.get("EMAIL")



                c = {
                    "email": entered_email,
                    'domain': '127.0.0.1:8000',
                    'site_name': 'Clubtastic',
                    "uid": urlsafe_base64_encode(force_bytes(entered_email)),
                    "user": u,
                    'token': default_token_generator.make_token(u),
                    'protocol': 'http',
                }
                message = render_to_string('authentication/registration_input_email', c)

                print("SENDING.....")
                print(entered_email)

                try:
                    send_mail('l', message, system_mail_email, [entered_email])
                    # send_mail(system_mail_email, system_mail_password, entered_email,
                    #           "Set Password", message)
                except TimeoutError:
                    return render(request, 'authentication/error.html', {
                        'error_message': "There was an error while sending you a reset email. Please try again later",

                    })

                print("SENTTTTTT")
                return render(request, 'authentication/password_reset_sent.html', {

                })

            else:
                print("Email doesn't exist")

    return render(request, 'authentication/enter_email.html', {
    })


def set_account_password(request, *args, **kwargs):
    email = kwargs.pop('user_email')
    user = User.objects.get(email=email)
    if request.method == "GET":
        set_password_form = SetPasswordForm()
        return render(request, 'authentication/password_reset_form.html', {
            'set_password_form': set_password_form,
        })
    else:
        print("elseeee")
        print(user)
        set_password_form = SetPasswordForm(request.POST)
        if set_password_form.is_valid():
            print("validdddd")
            user.set_password(set_password_form.cleaned_data['password'])
            user.save()
            return render(request, 'authentication/password_reset_done.html', {
                'set_password_form': set_password_form,

            })
        print("nottt validdd")
        print(set_password_form.errors)
    return render(request, 'authentication/password_reset_form.html', {
    })


def logout(request):
    django.contrib.auth.logout(request)
    return redirect('main_page')


def learn_more(request):
    return render(request, 'authentication/learn_more.html', {
    })


def faq(request):
    return render(request, 'authentication/faq.html', {
    })


def support(request):
    return render(request, 'authentication/support.html', {
    })

