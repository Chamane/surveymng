import json

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import FormSurvey, Question, Response, Survey

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
                user.set_password(form.cleaned_data["password"])
                user.save()
                messages.success(request, f"User {user.username} succesfully created")
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
            user = User.objects.filter(username__contains=lookup_value)
        except Exception:
            user = None
    else:
        user = None

    return render(request, "survey/agent_looking.html", {"agents": user})


def create_survey(request):
    return render(request, "survey/create_survey.html")


def survey_lookup(request):
    try:
        lookup_value = request.POST["lookup_value"]
    except Exception:
        lookup_value = None

    if lookup_value:
        try:
            surveys = Survey.objects.filter(title__contains=lookup_value)
        except Exception:
            surveys = None
    else:
        surveys = None

    return render(request, "survey/survey_looking.html", {"surveys": surveys})


def create_formsurvey(request):
    surveys = Survey.objects.all()
    return render(request, "survey/create_formsurvey.html", {"surveys": surveys})


def formsurvey_lookup(request):
    try:
        lookup_value = request.POST["lookup_value"]
    except Exception:
        lookup_value = None

    if lookup_value:
        try:
            formsurveys = FormSurvey.objects.filter(title__contains=lookup_value)
        except Exception:
            formsurveys = None
    else:
        formsurveys = None

    return render(
        request, "survey/search_formsurvey.html", {"formsurveys": formsurveys}
    )


def ajax_create_survey(request):
    surveyToCreate = json.load(request)["survey"]

    user = get_object_or_404(User, pk=request.user.pk)

    # print(surveyToCreate['title'])

    # create survey
    surveyCreated = Survey.objects.create(
        title=surveyToCreate["title"],
        description=surveyToCreate["description"],
        created_by=user,
    )

    for question in surveyToCreate["questions"]:
        Question.objects.create(
            title=question["title"],
            question_type=question["type"],
            survey=surveyCreated,
        )

    #
    messages.success(request, "L'enquête fut créer avec succès")

    return JsonResponse(surveyToCreate)


def ajax_get_questions(request):
    survey_id = int(json.load(request)["survey_id"])
    survey = get_object_or_404(Survey, pk=survey_id)
    questions = Question.objects.filter(survey__pk=survey_id)
    print(questions)
    data = {"survey_title": survey.title, "questions": []}
    for question in questions:
        questionObj = {
            "id": question.id,
            "title": question.title,
            "type": question.question_type,
        }
        data["questions"].append(questionObj)
    return JsonResponse(data)


def ajax_post_formsurvey(request):
    formsurvey = json.load(request)["formsurvey"]

    # get related survey
    survey = get_object_or_404(Survey, pk=formsurvey["survey"]["id"])

    # get related user
    user = get_object_or_404(User, pk=request.user.id)

    # create formsurvey
    get_formsurvey = FormSurvey.objects.create(
        title=formsurvey["formsurvey_title"], survey=survey, created_by=user
    )

    # create questions
    for question in formsurvey["questions"]:
        get_question = get_object_or_404(Question, pk=question["id"])
        Response.objects.create(
            form_survey=get_formsurvey, question=get_question, content=question["value"]
        )

    messages.success(request, "Formulaire de réponse enregistré avec succès")

    return JsonResponse(formsurvey)


def get_formsurvey(request, formsurvey_id):

    formsurvey = get_object_or_404(FormSurvey, pk=formsurvey_id)

    responses = Response.objects.filter(form_survey=formsurvey)

    return render(
        request,
        "survey/get_formsurvey.html",
        {"formsurvey": formsurvey, "responses": responses},
    )
