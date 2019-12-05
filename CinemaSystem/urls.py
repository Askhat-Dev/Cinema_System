from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += [
    path('MainPage/', include('catalog.urls')),

]


from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/MainPage/', permanent=True)),
]
path('accounts/', include('django.contrib.auth.urls')),
