from django import forms
from .models import Dog, STATUS, BOOKED, SEX, SIZE, Comment


class DogForm(forms.ModelForm):

    class Meta:
        model = Dog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

# Comment form

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)