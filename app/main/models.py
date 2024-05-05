from django.db import models

# Create your models here.
# models.py

from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LessonTopic(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)

    def __str__(self):
        return self.topic

class Lesson(models.Model):
    topic = models.ForeignKey(LessonTopic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Slide(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    content =  models.TextField()
    image = models.ImageField(upload_to='post',verbose_name='Фото', blank=True,)


    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ('id',)