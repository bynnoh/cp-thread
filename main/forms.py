
from django.forms import ModelForm, Textarea
from .models import Thread, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import FieldWithButtons, StrictButton

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content', 'image', 'topic']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'image']
        labels = {
            'content': '댓글',
            'image': '댓글 이미지 첨부'
        }
        widgets = {
            'content': Textarea(attrs={'cols': 10, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FieldWithButtons(
                'content',
                'image',
                StrictButton("댓글 작성", type="submit", css_class="btn-primary"),
            ),
        )
