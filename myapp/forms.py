# from django import forms
# from django import *
    
# class RegisterForm(forms.Form):
#     full_name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control" ,"placeholder":"Enter Your Name"}))
#     username=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username" }))
#     email=forms.EmailField(max_length=20,widget=forms.EmailInput(attrs={"class":"form-control" ,"placeholder":"Email Address"}))
#     password=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":" Password" }))
#     confirm_password=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={"class":"form-control" ,"placeholder":"Confirm_Password"}))

  
#     def clean(self):
#         cleaned_data = super().clean()
#         full_name = cleaned_data.get(full_name)

#         if full_name and len(full_name) < 4:
#             self.add_error('full_name'," Full Name Must be 4 Character")
