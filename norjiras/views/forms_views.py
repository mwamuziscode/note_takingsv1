from django import forms
from notes.models.profiles import Profile


class ProfileForm(forms.ModelForm):
    # pass
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'location', 'birth_date']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
