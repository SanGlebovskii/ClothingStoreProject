from django import forms

from .models import Order, Review

REVIEW_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_date'].label = 'Дата получения заказа'

    order_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone', 'address', 'buying_type', 'order_date', 'comment'
        )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rate', 'text')
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control shadow px-2', 'rows': 6}),
            'rate': forms.RadioSelect(choices=REVIEW_CHOICES)
        }


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000)
