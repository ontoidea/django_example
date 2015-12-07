from django import forms
 
class WriteForm(forms.Form):
    subject = forms.CharField(label='subject', max_length=100)
    content = forms.CharField(label='content', widget=forms.Textarea)