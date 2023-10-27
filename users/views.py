from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import SignupForm
from .tokens import account_activation_token

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import login

# Create your views here.
def registration(request):
    context = {}

    if request.method == 'POST':
        context["form"] = SignupForm(request.POST)

        if context["form"].is_valid():
            user = context["form"].save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activez votre compte sur Faces'

            # DEBUG
            print(f"\n!DEBUG! ***\nurlsafe_base64_encode(force_bytes(user.pk)).encode().decode():\n{urlsafe_base64_encode(force_bytes(user.pk)).encode().decode()}")
            # DEBUG
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = context["form"].cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'registration/confirmation.html')
    else:
        context["form"] = SignupForm()

    return render(request, 'registration/registration.html', context)


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return render(request, 'registration/activation_success.html', {})
    else:
        return render(request, 'registration/activation_fail.html', {})

class LoginWithPages(LoginView):
    pass