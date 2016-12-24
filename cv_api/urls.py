
from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib import admin
from face_detector import views

urlpatterns = [
    # Examples:

    url(r'^face_detection/detect/$', views.detect),

    # url(r'^$', 'cv_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
]
