from django import forms


class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Please verify your email address")
    suggestion = forms.CharField(widget=forms.Textarea)
    honey_pot = forms.CharField(required=False, widget=forms.HiddenInput, label="Leave empty", validators=[lambda x: len(x) == 0])

    def clean_honey_pot(self):
        if self.cleaned_data['honey_pot']:
            raise forms.ValidationError("Honey pot should be left empty. Bad bot!")
        return self.cleaned_data['honey_pot']
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify_email = cleaned_data.get('verify_email')

        if email != verify_email:
            raise forms.ValidationError("You need to enter the same email in both fields")
        return cleaned_data
