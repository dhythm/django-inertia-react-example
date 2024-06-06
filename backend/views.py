import django
from inertia import inertia


@inertia('Index/index')
def index(request):
    return {
        "services": [
            {
                "version": django.get_version(),
                "name": "Django",
                "url": "https://www.djangoproject.com/",
                "iconUrl": "https://github.com/django.png"
            }
        ]
    }