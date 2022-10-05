from django import forms

# from main.models import Survey


class AgentForm(forms.Form):
    username = forms.CharField(label="Username")
    fullname = forms.CharField(label="Nom complet")
    email = forms.EmailField()
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    re_password = forms.CharField(
        label="Re-entrer password",
        widget=forms.PasswordInput,
    )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     re_password = cleaned_data.get('re_password')

    #     print(password)
    #     print(re_password)

    #     if password == re_password:
    #        self.add_error('Password didnt match', re_password)


class SurveyForm(forms.Form):
    title = forms.CharField(label="Titre de l'enquete")
    description = forms.CharField(label="Description")


class QuestionForm(forms.Form):
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

    title = forms.CharField(label="Intitulé de la question")
    question_type = forms.ChoiceField(
        label="Type de la réponse attendue", choices=QUESTION_TYPE
    )


class OptionForm(forms.Form):
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

    content = forms.CharField(label="Contenu de l'option de réponse")
    option_type = forms.ChoiceField(
        label="Type de l'option de réponse", choices=OPTION_TYPE
    )


# class FormSurveyForm(forms.ModelForm):
#     class Meta:
#         model = models.FormSurvey
#         fields = ['title', 'description']

# class ResponseForm(forms.ModelForm):
#     class Meta:
#         model = models.Response
#         fields = ['content',]
