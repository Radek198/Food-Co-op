from django import forms
from django.core.validators import EmailValidator, URLValidator, ValidationError
from portal.models import MyUser, Koop, Supplier, Category, Product


from django.contrib.auth.forms import UserCreationForm




class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = MyUser
        fields = ('username', 'email', 'koop')

#class AddUserForm (forms.ModelForm):
#    password = forms.CharField(max_length=64, widget=forms.PasswordInput)
#    password1 = forms.CharField(max_length=64, widget=forms.PasswordInput)
#    email = forms.CharField(max_length=64, validators =[EmailValidator()])
#    class Meta:
#        model = MyUser
#        fields = ['nickname', 'email', 'kooperatywa', 'supplier', 'koopadmin', 'password', ]
#
#   def clean_username(self):
#       nickname = self.cleaned_data['nickname']
#       queryset = MyUser.objects.filter(nickname=nickname)
#       if queryset:
#          raise ValidationError("taki login juz istnieje")
#       return nickname
#   def clean(self):
#       password = self.cleaned_data['password']
#       password1 = self.cleaned_data['password1']
#       if password != password1:
#           raise ValidationError({'password': 'chasla nie sa identyczne'})
#       return self.cleaned_data


class AddKoopForm (forms.ModelForm):
    email = forms.CharField(max_length=64, validators=[EmailValidator()])
    class Meta:
        model = Koop
        fields = ['name', 'email', 'city']
    def clean_name(self):
        name = self.cleaned_data['name']
        queryset = Koop.objects.filter(name=name)
        if queryset:
           raise ValidationError("kooperatywa juz zarejestrowana")
        return name


class EditKoopForm (forms.ModelForm):
    email = forms.CharField(max_length=64, validators=[EmailValidator()])
    District= forms.CharField(max_length=64, required = False)
    Phone = forms.CharField(max_length=64, required = False)


    class Meta:
        model = Koop
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        queryset = MyUser.objects.filter(name=name)
        if queryset:
            raise ValidationError("kooperatywa juz zarejestrowana")
        return name


class SearchForm(forms.Form):
    search = forms.CharField(label="search", max_length=255)


class AddSupplierForm (forms.ModelForm):
    email = forms.CharField(max_length=64, validators=[EmailValidator()])
    class Meta:
        model = Supplier
        fields = '__all__'



class AddCategoryForm (forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class AddProductForm (forms.ModelForm):
  #  category = forms.CharField(max_length=64)
  #  supplier = forms.CharField(max_length=64)
    class Meta:
        model = Product
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)

class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    koop = forms.ModelChoiceField(queryset=Koop.objects.order_by('name'), empty_label="(Nothing)")

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'first_name', 'last_name', 'koop']


    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and MyUser.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('Podaj inny adres e-mail')
        return email


