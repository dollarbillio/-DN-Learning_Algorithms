from django.conf.urls import url
from django.contrib import admin
from .views import home_page    # added

urlpatterns = [
    # Added 
	url(r'^$', home_page),      # added
    url(r'^admin/', admin.site.urls)
]

