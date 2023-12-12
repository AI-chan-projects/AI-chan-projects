settings.py루트 staticfiles 디렉토리를 추가하기.

```
   STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
        ]
```

/static/images/favicon.ico 추가


템플릿(base.html)에 파비콘을 추가하세요.

```
{% load static %}
<link rel="shortcut icon" type="image/png" href="{% static 'images/favicon.ico' %}"/>
```


urls.py그리고 브라우저가 파비콘을 찾기 때문에 URL 리디렉션을 생성하세요.

```
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    ...
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico')))
]
```