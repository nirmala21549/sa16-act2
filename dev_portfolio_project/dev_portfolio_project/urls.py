# dev_portfolio_project/urls.py

from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),  # Include portfolio app URLs
]
