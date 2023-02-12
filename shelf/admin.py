from django.contrib import admin

from .models import Book
from .models import Author
from .models import Genre
from .models import Language

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
