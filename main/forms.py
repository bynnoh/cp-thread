
from django.forms import ModelForm, Textarea
from .models import Thread, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from crispy_forms.bootstrap import FieldWithButtons, StrictButton

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content', 'image', 'topic']
        widgets = {
            'content': Textarea(attrs={'cols': 12, 'rows': 3}),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'image']
        labels = {
            'content': '댓글',
            'image': '댓글 이미지 첨부'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['content'].widget.attrs = {'cols': 100, 'rows': 3}
        self.helper.layout = Layout(
            FieldWithButtons(
                'content',
                StrictButton("댓글 작성", type="submit", css_class="btn-primary"),
            ),
            Field('image')
        )
