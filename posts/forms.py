from django import forms
from posts.models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author','image','description' ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].initial = self.initial['user'].id
        self.fields['author'].widgets = forms.widgets.HiddenInput()
        