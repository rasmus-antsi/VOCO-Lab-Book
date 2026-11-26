"""
URL configuration for _core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('a_main.urls')),
    path('accounts/', include('a_accounts.urls')),
    path('inventory/', include('a_inventory.urls')),
    path('bookings/', include('a_bookings.urls')),
    path('loans/', include('a_loans.urls')),
    path('incidents/', include('a_incidents.urls')),
    path('audit/', include('a_audit.urls')),
    path('api/agent/', include('a_agent.urls')),  # becomes the Django Ninja API in phase 3
]
