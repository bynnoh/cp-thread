from django import forms
from django.forms import ModelForm
from .models import Thread, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from crispy_forms.bootstrap import FieldWithButtons, StrictButton

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content', 'image', 'topic']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 12, 'rows': 3}),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'image']
        labels = {
            'content': '',
            'image': ''
        }
        widgets = {
            'image': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['content'].widget.attrs = {'cols': 100, 'rows': 2,}
        self.helper.layout = Layout(
            Div(
                Div(FieldWithButtons(
                'content',
                StrictButton("작성", type="submit", css_class="btn-primary"),
            ), css_class="p-0"), Div('image', css_class="col-2 p-0")),
        )
