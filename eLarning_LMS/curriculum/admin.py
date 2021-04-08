from django.contrib import admin
from curriculum.models import standard,lesson,subject,comment,reply

# Register your models here.
admin.site.register(subject)
admin.site.register(standard)
admin.site.register(lesson)
admin.site.register(comment)
admin.site.register(reply)