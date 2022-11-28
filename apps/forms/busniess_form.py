from django import forms

from apps.core.models import Business


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['updated_at', 'created_at', 'uuid']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'