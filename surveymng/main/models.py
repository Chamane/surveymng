from django.db import models

from surveymng.users.models import User


class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model):
    DATE = "DT"
    HEURE = "HR"
    NOMBRE = "NB"
    TEXTE = "TX"

    QUESTION_TYPE = [
        (DATE, "Date"),
        (HEURE, "Heure"),
        (NOMBRE, "Nombre"),
        (TEXTE, "Texte"),
    ]

    title = models.CharField(max_length=255)
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPE, default=TEXTE)
    date_created = models.DateTimeField(auto_now_add=True)
    survey = models.ForeignKey(
        Survey, on_delete=models.CASCADE, related_name="questions"
    )

    def __str__(self):
        return self.title


class Option(models.Model):
    DATE = "DT"
    HEURE = "HR"
    NOMBRE = "NB"
    TEXTE = "TX"

    OPTION_TYPE = [
        (DATE, "Date"),
        (HEURE, "Heure"),
        (NOMBRE, "Nombre"),
        (TEXTE, "Texte"),
    ]

    content = models.CharField(max_length=255)
    option_type = models.CharField(max_length=2, choices=OPTION_TYPE, default=TEXTE)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="options"
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class FormSurvey(models.Model):
    title = models.CharField(max_length=255)
    survey = models.ForeignKey(
        Survey, on_delete=models.CASCADE, related_name="formsurveys"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="formsurveys"
    )

    def __str__(self):
        return self.title


class Response(models.Model):
    form_survey = models.ForeignKey(
        FormSurvey, on_delete=models.CASCADE, related_name="responses"
    )
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="responses"
    )
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.question.title
