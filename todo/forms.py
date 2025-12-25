from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task name pls'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Task description pls'}),
            'rows': 5,
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input', 'placeholder': 'Checkbox?'}),
        }

        labels = {
            'title': 'Task name',
            'description': 'Task description',
            'completed': 'Completed or not',
        }
