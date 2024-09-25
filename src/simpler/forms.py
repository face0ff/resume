from django.forms import TimeInput, DateInput, modelformset_factory
from src.simpler.models import *
from django import forms


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'photo-upload'}),
            'name': forms.Textarea(attrs={'rows': 1, 'class': 'form-control'}),
            'surname': forms.Textarea(attrs={'rows': 1, 'class': 'form-control'}),
            'patronymic': forms.Textarea(attrs={'rows': 1, 'class': 'form-control'}),
            'email': forms.Textarea(attrs={'rows': 1, 'class': 'form-control'}),
            'position': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'salary': forms.Textarea(attrs={'rows': 1, 'class': 'form-control'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['date'].initial = datetime.datetime.today().strftime('%d.%m.%Y')
    #     self.fields['time'].initial = datetime.datetime.today().strftime('%H:%M')
    #     self.fields['master'].empty_label = 'Выберите...'
    #     self.fields['master'].queryset = UserProfile.objects.filter(is_staff=False, role__isnull=False)
    #     self.fields['apartment'].empty_label = 'Выберите...'

    # owner = forms.ModelChoiceField(
    #     required=False,
    #     widget=forms.Select(
    #         attrs={'class': 'form-control', 'onchange': "selectUser(this)"}),
    #     queryset=UserProfile.objects.filter(role_id__isnull=True),
    #     empty_label="Выберите..."
    # )

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('title', 'description')
        exclude = ('resume',)

EducationFormSet = modelformset_factory(Education, form=EducationForm, extra=0, can_delete=True)