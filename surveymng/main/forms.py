from django import forms


class AgentForm(forms.Form):
    username = forms.CharField(label="Username", max_length=255)
    fullname = forms.CharField(label="Nom complet", max_length=255)
    email = forms.EmailField()
    password = forms.CharField(
        label="Password", max_length=255, widget=forms.PasswordInput
    )
    re_password = forms.CharField(
        label="Re-entrer password", max_length=255, widget=forms.PasswordInput
    )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     re_password = cleaned_data.get('re_password')

    #     print(password)
    #     print(re_password)

    #     if password == re_password:
    #        self.add_error('Password didnt match', re_password)
