from django import forms
from curriculum.models import lesson

class createLessonForm(forms.ModelForm):
    class Meta:
        model = lesson
        fields = ('lesson_id','name','position','video','ppt','notes')