import random
import string
from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 10)

def code_generator(size=SHORTCODE_MIN):
    return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(size))

def create_shortcode(instance, size=SHORTCODE_MIN):
    print(instance)
    new_code = code_generator(size=size)
    klass = instance.__class__
    qs_exists = klass.objects.filter(shortcode=new_code).exists()
    if (qs_exists):
        return create_shortcode(size=size)
    return new_code