from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render

from . import forms

User = get_user_model()


def index(request):
    return redirect("account_login")


def create_agent(request):
    if request.method == "POST":
        form = forms.AgentForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["password"] == form.cleaned_data["re_password"]:
                user = User(
                    username=form.cleaned_data["username"],
                    name=form.cleaned_data["fullname"],
                    email=form.cleaned_data["email"],
                )
                user.save()
                user.set_password(form.cleaned_data["password"])
                messages.success(request, "User succesfully created")
                return redirect("users:detail", username=request.user.username)
            else:
                messages.error(request, "Password didnt match")
    else:
        form = forms.AgentForm()

    return render(request, "survey/create_agent.html", {"form": form})


def agent_looking(request):
    try:
        lookup_value = request.POST["lookup_value"]
    except Exception:
        lookup_value = None

    if lookup_value:
        try:
            user = User.objects.get(username=lookup_value)
        except Exception:
            user = None
    else:
        user = None

    return render(request, "survey/agent_looking.html", {"agent": user})


def create_survey(request):
    pass


def create_formsurvey(request):
    pass
