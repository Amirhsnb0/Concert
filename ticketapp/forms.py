from django import forms
from .models import concertModel

class searchform (forms.Form):
    searchtext=forms.CharField( max_length=299 , required=False, label="جستوجو")


class ConcertForm(forms.ModelForm):
    
    class Meta:
        model=concertModel
        fields=['Name','SingerName','length','Poster']
        #exclude=["Poster"]