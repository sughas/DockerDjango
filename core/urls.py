from django.contrib import admin
from django.urls import path

from core.hello import myView

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns=[
    path('HelloWorld/',myView)
]