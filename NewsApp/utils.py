import random, string
from email_validator import validate_email, EmailNotValidError
from django.core.mail import send_mail
from datetime import datetime, timezone
from django.core.mail import EmailMessage

OTP_LENGTH = 4
OTP_TIMEOUT = 300
TRANS_LENGTH = 12

def randomDigits(stringLength=OTP_LENGTH):
    '''
    -Generate a random string of letters and digits
    '''
    return ''.join(random.choice(string.digits) for i in range(stringLength))

def isEmail(email):
    '''
    -checks the input string is valid email or not
    -returns true if valid email, false otherwise
    '''
    try:
        v = validate_email(email)
        return True
    except EmailNotValidError:
        return False

def sendMailOtp(email):
    '''
    -generates  otp and send to the given email
    -returns the otp
    '''
    otp = randomDigits()
    messageBody = 'Your one time password is: ' + otp
    sent = send_mail(
        'Password reset for ' + email,
        messageBody,
        'noreply@fantex.com',
        [email],
        fail_silently=False,
        )
    if sent == 1:
        return otp
    else:
        return None

def sendMail(email, email_data, mail_subject):
    '''
        to send email verification link
    '''
    email = EmailMessage(
                        mail_subject,
                        email_data,
                        to=[email]
            )
    email.send()
    return True
