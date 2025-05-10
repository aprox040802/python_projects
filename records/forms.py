from django import forms
from .models import Record
from datetime import date

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'price', 'quantity', 'date_of_entry', 'description']
        widgets = {
            'date_of_entry': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': '0.01',
                'placeholder': '$0.00'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': '1',
                'placeholder': '0'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default date to today for new records
        if not self.instance.pk:  # Only for new records
            self.initial['date_of_entry'] = date.today()
        
        # Add currency symbol to price field label
        self.fields['price'].label = 'Price ($)'
        
        # Add validation for price
        self.fields['price'].validators.append(self.validate_price)
        
    def validate_price(self, value):
        if value < 0:
            raise forms.ValidationError('Price cannot be negative')
        return value