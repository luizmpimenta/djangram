from django.conf import settings
from templated_email import send_templated_mail
from django.conf import settings

def send_confirm_user_signup_email(user):
    kwargs = dict(
        template_name='signup_user',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        context={
            'user': user,
            
           },
) 
    return send_templated_mail(**kwargs)

