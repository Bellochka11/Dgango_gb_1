from django import forms
import datetime

class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)


class ManyFieldsForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18)
    height = forms.FloatField()
    is_active = forms.BooleanField(required=False) #required=False - если лож то у поля нет галочки
    birthdate = forms.DateField(initial=datetime.date.today) #сегодняшняя дата
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')]) #выбор m для сервера male визуально для пользователя


class ManyFieldsFormWidget(forms.Form):
    name = forms.CharField(max_length=50,
                            widget = forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',
                                                             'placeholder': 'user@mail.ru'}))
    age = forms.IntegerField(min_value=18,
                            widget = forms.NumberInput(attrs={'class': 'form-control'}))
    height =forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False,
                                    widget = forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    birthdate = forms.DateField(initial=datetime.date.today,
                                widget = forms.DateInput(attrs={'class': 'form-control',
                                                                'type':'date'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')],
                                widget = forms.RadioSelect(attrs={'class': 'form-check-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)

    def clean_name(self):
        """Плохой пример. Подмена параметра min_length."""
        name = self.cleaned_data['name']
        if len(name) < 3:   
            raise forms.ValidationError('Имя должно содержать не менее 3 символов')
        return name

    def clean_email(self):
        email: str = self.cleaned_data['email']
        if not (email.endswith('vk.mail.ru') or email.endswith('corp.mail.ru')): #если почта не оканчивается конец на это
            raise forms.ValidationError('Используйте корпоративную почту')
        return email
    
class ImageForm(forms.Form):
    image = forms.ImageField()