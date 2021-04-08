from django import forms
from curriculum.models import lesson,comment,reply

class createLessonForm(forms.ModelForm):
    class Meta:
        model = lesson
        fields = ('lesson_id','name','position','video','ppt','notes')




class commentForm(forms.ModelForm):
    class Meta:
        model =comment
        fields = ('body',)
        labels = {"body": 'comment:'}

        widgets={
            'body': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'cols':70, 'placeholder':"Enter Your Comment"}),
        }
    '''
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(commentForm,self).__init__(*args, **kwargs)
    '''

class replyForm(forms.ModelForm):
    class Meta :
        model = reply
        fields= ('reply_body',)
        widgets={
            'reply_body': forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':10}),
 
        }
    '''
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(replyForm,self).__init__(*args, **kwargs)
    '''
