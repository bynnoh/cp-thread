
from django.forms import ModelForm, Textarea
from .models import Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import FieldWithButtons, StrictButton

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': ''
        }
        widgets = {
            'content': Textarea(attrs={'cols': 10, 'rows': 1}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FieldWithButtons(
                'content',
                StrictButton("댓글 작성", type="submit", css_class="btn-primary")
            ),
        )
