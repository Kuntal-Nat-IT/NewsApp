import secrets
import string
import os
import sys
import hashlib
import socket
import httpagentparser


def Big_Number_Generator():
    letters = string.ascii_letters + string.digits + string.hexdigits
    l = [secrets.choice(letters) for i in range(20)]
    num = ''
    for i in l:
        num = num + i

    return num


def HideMyData(data):
    result = ''
    result = hashlib.sha256(data.encode())
    return result.hexdigest()


def GetIPLocationPC(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def DetectBrowser(request):
    agent = request.environ.get('HTTP_USER_AGENT')
    browser = httpagentparser.detect(agent)
    if not browser:
        browser = agent.split('/')[0]
    else:
        browser_name = browser['browser']['name'] 
        browser_version = browser['browser']['version']
        browser = browser_name + " " + browser_version

    return browse

