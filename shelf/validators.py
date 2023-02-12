from django.core.exceptions import ValidationError

def long_name(value):
    if len(value) < 5:
        raise ValidationError("name must be at least 5 characters long")
