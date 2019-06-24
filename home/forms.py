from django import forms
from home.models import Book,Author,Genre,Student

class CustomForms(forms.Form):
    # username= forms.CharField(
    #     label='Username',
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder':'Your username',
    #             'class':'form-control'
                
    #         }
    #     )
    # )
    # email=forms.EmailField(label='your Email',widget=forms.EmailInput(attrs={'placeholder':'ac@email.com','class':'form-control'})
    #)

    name=forms.CharField(label='Book name', widget=forms.TextInput(attrs={'maxlength':'30','placeholder':'Book Name','class':'form-control'}))
    book_author=forms.ModelChoiceField(queryset=Author.objects.all(),empty_label='Author',widget=forms.Select(attrs={'name':'author','id':'author','class':'form-control'}))
    purchase_date=forms.DateField(label='',widget=forms.DateInput(attrs={'placeholder':'Purchase Date','name':'date','id':'date','class':'form-control'}))
    # summary=forms.CharField(label='summary',widget=forms.Textarea(attrs={'placeholder':'summary','name':'summary','id':'summary','class':'form-control'}))
    # isbn=forms.CharField(label='ISBN Number',widget=forms.TextInput(attrs={'placeholder':'ISBN Number','class':'form-control','name':'isbn','id':'isbn'}))
    # genre=forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),widget=forms.CheckboxSelectMultiple)

class ModelBookForms(forms.ModelForm):
    name=forms.CharField(label='Book name', widget=forms.TextInput(attrs={'maxlength':'30','placeholder':'Book Name','class':'form-control'}))
    book_author=forms.ModelChoiceField(queryset=Author.objects.all(),empty_label='Author',widget=forms.Select(attrs={'name':'author','id':'author','class':'form-control'}))
    summary=forms.CharField(label='summary',widget=forms.Textarea(attrs={'placeholder':'summary','name':'summary','id':'summary','class':'form-control'}))
    isbn=forms.CharField(label='ISBN Number',widget=forms.TextInput(attrs={'placeholder':'ISBN Number','class':'form-control','name':'isbn','id':'isbn'}))
    genre=forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Book 
        fields='__all__'

class SearchForm(forms.Form):
   q=forms.CharField(label='',widget=forms.TextInput(attrs={'maxlength':'30','placeholder':'search','class':'form-control','minlength':'2'}))
