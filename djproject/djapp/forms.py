from django import forms

class RegistrationForm(forms.Form):
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)
    # user_name = forms.CharField(max_length=100)
    # password = forms.CharField(max_length=100)
    # mobile = forms.IntegerField()
    # email = forms.EmailField()
    first_name = forms.CharField(
        label="Enter First Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'First Name',
                'class':'form-control'
            }
        )
    )
    last_name = forms.CharField(
        label="Enter Your Last Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Last Name',
                'class':'form-control'
            }
        )
    )
    user_name = forms.CharField(
        label="Enter Your USerName",
        widget=forms.TextInput(
            attrs={
                'placeholder':'UserName',
                'class':'form-control'
            }
        )
    )
    password = forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class':'form-control'
            }
        )
    )
    mobile = forms.CharField(
        label="Enter Your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Mobile Number',
                'class':'form-control'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email ID",
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Email ID',
                'class':'form-control'
            }
        )
    )

class LoginForm(forms.Form):
    user_name = forms.CharField(
        label="Enter Your USerName",
        widget=forms.TextInput(
            attrs={
                'placeholder':'User Name',
                'class':'form-control'
            }
        )
    )
    password = forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class':'form-control'
            }
        )
    )

class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    rating = forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Your Rating',
                'class':'form-control'
            }
        )
    )
    feedback = forms.CharField(
        label="Enter Your Feedback",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Feedback'
            }
        )
    )
from multiselectfield import MultiSelectFormField
class ContactForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter Your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile Number'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email ID'
            }
        )
    )

    COURSES_CHOICES = (
        ('Python', 'PYTHON'),
        ('Django', 'DJANGO'),
        ('Ui', 'UI'),
        ('RestAPI', 'REST API')
    )
    courses = MultiSelectFormField(choices=COURSES_CHOICES,label="Select Required Courses:")

    TRAINER_CHOICES = (
        ('Sai', 'SAI'),
        ('Nani', 'NANI'),
        ('Satya', 'SATYA')
    )
    trainers = MultiSelectFormField(choices=TRAINER_CHOICES, label="Select Required Trainers:")

    BRANCHES_CHOICES = (
        ('Hyd', 'HYDERABAD'),
        ('Bang', 'BANGALORE'),
        ('Pune', 'PUNE')
    )
    branches = MultiSelectFormField(choices=BRANCHES_CHOICES, label="Select Required Branches:")

    date = forms.DateField(
        widget=forms.SelectDateWidget(),label="Enter Your Date:"
    )

    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female')
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect,choices=GENDER_CHOICES,label="Select Your Gender:"
    )



