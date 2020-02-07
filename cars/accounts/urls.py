from django.urls import include, path

urlpatterns = [
    path(r'', include('djoser.urls')),
    path(r'', include('djoser.urls.authtoken')),
]