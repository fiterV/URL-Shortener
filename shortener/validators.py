from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(value):
    url_validator = URLValidator()
    print(value)
    try:
        url_validator(value)
    except:
        print("Error during URL validation in shortener")
        raise ValidationError("Invalid URL given")

    return value