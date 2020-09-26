from django.contrib import admin
from django.urls import path
from employee import views
from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp', include('views.urls')),

]
