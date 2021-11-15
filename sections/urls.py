from django.urls import path

from sections.views import IndexView

app_name = 'sections'

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]