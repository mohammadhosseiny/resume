from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class ContactForm_Fa(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='نام')

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='ایمیل')

    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='موضوع')

    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='پیام')
