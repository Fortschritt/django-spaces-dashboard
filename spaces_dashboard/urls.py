from django.conf.urls import url
from spaces.urls import space_patterns

from . import views

app_name = 'spaces_dashboard'
urlpatterns = (
    url(r'^$', views.dashboard, name='dashboard'),
)