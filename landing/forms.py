from django import forms
from .models import Lead


class LeadForm(forms.ModelForm):
    class Meta:  # изменение поведения модели
        model = Lead  # связка формы LeadForm с моделью Lead
        fields = ['name', 'last_name', 'phone_number']  # перечисление необходимых полей. которые будут показываться на экране
