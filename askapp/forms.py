# coding=utf-8
from django import forms
from django.forms import ModelForm
from django.db import models
from models import Question, Answer, Tag

from django.contrib.admin import widgets


'''class AddQuestionForm(forms.Form):
    head = forms.CharField(
        max_length=50,
        error_messages={'required': 'Describe your question shortly.'},
        label=''
    )
    content = forms.CharField(
        widget=forms.Textarea,
        error_messages={'required': "Ask something."},
        label=''
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        error_messages={'required': 'Add some tags.'},
        label='',
        help_text=''
    )'''


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
