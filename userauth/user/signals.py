from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.views.decorators.csrf import csrf_exempt

# @receiver(user_logged_in, sender=User)
@csrf_exempt
def user_set_session(sender, request, user, **kwargs):
    print(user.username)
    request.session['name'] = user.username
    if 'name' in request.session:
        print(request.session['name'])
user_logged_in.connect(user_set_session, sender=User)


@receiver(user_logged_out, sender=User)
def user_del_session(sender, request, user, **kwargs):
    del request.session['name']
    if 'name' in request.session:
        print(request.session['name'])
    print('bye')


@receiver(user_login_failed)
def user_login_fail(sender, credentials, request, **kwargs):
    print('credintials:', credentials)
    print('login failed')