from django import forms
from .models import Items

#flag choices
CHOICE = (
        ('BOUGHT', 'BOUGHT'),
        ('NOT AVAILABLE', 'NOT AVAILABLE'),
        ('PENDING', 'PENDING'),
    )


class AddItemForm(forms.ModelForm):
    '''
    creating form class for creating form fields to add items or update items
    '''
    name = forms.CharField(max_length=50, required=True)
    quantity = forms.CharField(max_length=20, required=True)
    status = forms.ChoiceField(choices=CHOICE, required=True)
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=True)

    class Meta:
        '''
        class for defining which model and fields want to use
        '''
        model = Items
        fields = ['name', 'quantity', 'status', 'date',  ]
        exclude = ['user', ]
