from django.contrib import admin
from django.urls import path
from users.views import signin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/signin', signin)
]
