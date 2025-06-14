from django.contrib import admin
from django.urls import path
from anushkaapp import views


urlpatterns = [
    path('anuu',views.home),
    path('admin/', admin.site.urls),
]
