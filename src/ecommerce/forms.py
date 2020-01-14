from django import forms

class ContactForm(forms.Form):

    fullname = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control",
               "id": "form_full_name",
               "placeholder": "Full Name"}
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control",
               "id": "form_full_name",
               "placeholder": "Email Address"}
    ))
    content = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control",
               "id": "form_full_name",
               "placeholder": "Your contents"}))

    def clean_email(self):
        email=self.cleaned_data.get("email")
        if not 'gmail.com' in email:
            raise forms.ValidationError("enter a valid gmail address")
        return email

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    email=forms.CharField(widget=forms.EmailInput())
    mobile=forms.CharField(widget=forms.NumberInput())
    Cpassword = forms.CharField(label="Confirm password",widget=forms.PasswordInput())

    def clean(self):
        data=self.cleaned_data
        password=data.get("password")
        cpassword=data.get("Cpassword")
        if password != cpassword:
            raise forms.ValidationError("Passowrd must match")
        else :
            return data



