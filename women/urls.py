from .views import *
from django.urls import path, re_path

urlpatterns = [
    path('', index, name="home"), #http://127.0.0.1/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    path('cats/<int:cat>/', categories),  # http://127.0.0.1/cats/1/
    path('cats/<slug:cat>/', categories),  # slug - a-z + "-" + "_"
    path('cats/<uuid:cat>/', categories),  # uuid - цифры + a-z + "/"
    path('cats/<path:cat>/', categories),  # path -любая строка + "/"
    path('cats/<str:cat>/', categories)  # str - люьая строка кроме символа "/"
]