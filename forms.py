from django import forms

class presForm(forms.Form):
    uid = forms.IntegerField()
   

class doctorprofileForm(forms.Form):
    did = forms.IntegerField()
   
class patientprofileForm(forms.Form):
    uid = forms.IntegerField()
    mobile_no = forms.IntegerField()
   
   
