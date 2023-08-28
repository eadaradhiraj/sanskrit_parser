from django import forms

class TextInputForm(forms.Form):
    # text_input = forms.Textarea()
    message = forms.CharField(widget=forms.Textarea)