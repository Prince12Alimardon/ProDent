from django.db import models


# Create your models here.


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(TimeStampModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Tag(TimeStampModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Post(TimeStampModel):
    title = models.CharField(max_length=212)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='posts')
    description = models.TextField()

    def __str__(self):
        return self.title


class Subscribe(TimeStampModel):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Doctors(TimeStampModel):
    name = models.CharField(max_length=212)
    profession = models.CharField(max_length=212)
    image = models.ImageField(upload_to='doctors')
    
    def __str__(self):
        return self.name


class Service(TimeStampModel):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='services')
    description = models.TextField()

    def __str__(self):
        return self.title
