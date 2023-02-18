# library
```
repo: https://github.com/sucmar/library.git
by: marco antonio baltazar santos
email: mabsbaltazar@gmail.com
```

## Api Root
```
{
    "genre": "http://127.0.0.1:8000/shelf/genre/",
    "language": "http://127.0.0.1:8000/shelf/language/",
    "author": "http://127.0.0.1:8000/shelf/author/",
    "book": "http://127.0.0.1:8000/shelf/book/"
}
```

## REQUERIMIENTOS

#### aplications
- library > shelf

#### models
- Author
- Genre
- Language
- Book

#### validaciones personalizadas
- long_name
show up the validation `name must be at least 5 characters long`

#### models registrados en admin
- Author
- Genre
- Language
- Book

#### ModelViewSet
- GenreViewSet
- LanguageViewSet
- AuthorViewSet
- BookViewSet

#### Custom API
- GenreCustomAPI


route
```
http://127.0.0.1:8000/shelf/genres/<str:name>    ===>     http://127.0.0.1:8000/shelf/genres/?name=Comedy
http://127.0.0.1:8000/shelf/genres/
```


#### requeriments.txt

```
asgiref==3.6.0
Django==4.1.7
djangorestframework==3.14.0
pytz==2022.7.1
sqlparse==0.4.3
tzdata==2022.7
```
