# coding=utf-8
from django import forms


def clean_tags(self):
    value = self.cleaned_data['tags']
    if len(value) > 3:
        raise forms.ValidationError("Don't add more than 3 tags.")
    return value


class AddAnswerForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea,
        label=''
    )


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)


class ValidAnswerForm(forms.Form):
    validity = forms.BooleanField(widget=forms.HiddenInput(), initial=False, required=False)
    a_id = forms.CharField(max_length=100, widget=forms.HiddenInput())
