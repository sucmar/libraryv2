from django.db import models
from .validators import long_name
from django.core.validators import RegexValidator

#Author MODEL
class Author(models.Model):
    firstname = models.CharField(max_length=100, validators=[long_name, RegexValidator(
                regex='^[a-zA-Z ]+$',
                message='Name must be a string'
            ), ])
    lastname = models.CharField(max_length=100, validators=[long_name, RegexValidator(
                regex='^[a-zA-Z ]+$',
                message='Name must be a string'
            ), ])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

#Genre MODEL
class Genre(models.Model):
    name = models.CharField(max_length=100, validators=[long_name, RegexValidator(
                regex='^[a-zA-Z ]+$',
                message='Name must be a string'
            ), ])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

#Language MODEL
class Language(models.Model):
    name = models.CharField(max_length=100, validators=[long_name, RegexValidator(
                regex='^[a-zA-Z]+$',
                message='Name must be a string'
            ), ])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

#Book MODEL
class Book(models.Model):
    title = models.CharField(max_length=100, validators=[long_name, RegexValidator(
                regex='^[a-zA-Z ]+$',
                message='Name must be a string'
            ), ])
    summary = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
