from django.conf.urls import url
from endpoint import views

urlpatterns = [
    url(r'^hellolancer$',
        views.SimpleView.as_view()),
]
