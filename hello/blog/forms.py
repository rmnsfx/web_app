from django import forms
from blog.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
        labels = {'description': ('Sample rate, Hz:'), 'document': ('')}
        #widgets = {'description': forms.Textarea(attrs={'placeholder': 'Search'}),}
        #field_classes = {'description': SRField,}

		
	#docfile = forms.FileField( label='Select a file' )
