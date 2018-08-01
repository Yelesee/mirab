from django import forms

class Calculate(forms.Form):
	mark = forms.IntegerField(label='mark')
	study = forms.IntegerField(label='study')
	hardness = forms.IntegerField(label='hardness')
	sysmark = forms.IntegerField(label='systemic mark')

class Mark(forms.Form):
	hesaban = forms.IntegerField(label='hesaban')
	hendese = forms.IntegerField(label='hendese')
	arabi = forms.IntegerField(label='arabi')