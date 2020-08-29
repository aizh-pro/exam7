
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible

from webapp.models import Poll


@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
    code = 'too_short'

    def compare(self, value, limit):
        return value < limit

    def clean(self, value):
        return len(value)


@deconstructible
class MaxLengthValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be max %(limit_value)d symbols long!'
    code = 'too_long'

    def compare(self, value, limit):
        return value > limit

    def clean(self, value):
        return len(value)


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']


    def clean(self):
        cleaned_data = super().clean()
        errors = []
        question = cleaned_data.get('question')
        if errors:
            raise ValidationError(errors)
        return cleaned_data


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ['name', 'description','start_date', 'end_date']
#
#     def clean(self):
#         cleaned_data = super().clean()
#         errors = []
#         description = cleaned_data.get('description')
#         name = cleaned_data.get('name')
#         start_date = cleaned_data.get('start_date')
#         end_date = cleaned_data.get('end_date')
#         if description and name and description == name:
#             errors.append(ValidationError("Text  should not duplicate it's name!"))
#         if errors:
#             raise ValidationError(errors)
#         return cleaned_data


