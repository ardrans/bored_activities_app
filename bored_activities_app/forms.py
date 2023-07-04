from django import forms


class EditForm(forms.Form):
    activity = forms.CharField(label='title', max_length=100)

