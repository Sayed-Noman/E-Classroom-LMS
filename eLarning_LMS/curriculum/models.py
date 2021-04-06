from django.db import models
from  django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class standard(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True,blank=True)
    description = models.TextField(max_length=550,blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


def save_subject_image(instance,filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]
    #get filename
    if instance.subject_id:
        filename = 'Subject_Pictures/{}'.format(instance.subject_id,ext)
    return os.path.join(upload_to, filename)

class subject(models.Model):
    subject_id =models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True,blank=True)
    standard = models.ForeignKey(standard,on_delete = models.CASCADE, related_name='subjects')
    image = models.ImageField(upload_to = save_subject_image,blank=True,verbose_name ='subject image')
    description = models.TextField(max_length=550, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject_id)
        super().save(*args, **kwargs)



def save_lesson_files(instance,filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]
    #get filename
    if instance.lesson_id:
        filename = 'lesson_files/{}/{}.{}'.format(instance.lesson_id,instance.lesson_id,ext)
        if os.path.exists(filename):
            new_name = str(instance.lesson_id) + str('1')
            filename = 'lesson_images/{}/{}.{}'.format(instance.lesson_id, new_name,ext)
    return os.path.join(upload_to, filename)


class lesson(models.Model):
    lesson_id = models.CharField(max_length=100, unique=True)
    standard = models.ForeignKey(standard,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    subject= models.ForeignKey(subject, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=150)
    position = models.PositiveSmallIntegerField(verbose_name= 'Chapter No')
    slug = models.SlugField(null=True,blank=True)
    video = models.FileField(upload_to=save_lesson_files,verbose_name='video',blank=True,null=True)
    ppt = models.FileField(upload_to=save_lesson_files,verbose_name='ppt',blank=True)
    notes = models.FileField(upload_to=save_lesson_files,verbose_name='notes',blank=True)

    class Meta:
        ordering = ['position']
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    

