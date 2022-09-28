from django.shortcuts import redirect


def index(request):
    return redirect("account_login")
