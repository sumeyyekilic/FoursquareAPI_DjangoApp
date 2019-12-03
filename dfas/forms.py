from django import forms
#MODELİ İMPORT
from .models import QueryModel

class QueryForm(forms.ModelForm):
	class Meta:
		model =QueryModel
		fields = {
			'venue',
			'location',
			'limit'
		}


	def __init__(self, *args, **kwargs):

		super(QueryForm, self).__init__(*args, **kwargs)
		self.fields['venue'].widget.attrs['placeholder'] = 'bir mekan türü gir..'
		self.fields['location'].widget.attrs['placeholder']='aranılan konumu gir...'
		self.fields['limit'].widget.attrs['placeholder']='listelenecek mekan limiti gir..'