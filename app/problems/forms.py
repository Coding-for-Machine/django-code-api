from django import forms

from .models import Problems

class ProblemsForm(forms.ModelForm):
    class Meta:
        model = Problems
        fields = ('name','body', 'slug', 'active', 'category', 'function_or_class_name', 'language', 'tag','user', 'status')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control','autocomplete': 'off'})
        
        self.fields['body'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['body'].required = False

