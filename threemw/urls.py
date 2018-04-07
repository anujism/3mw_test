"""threemw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from sites.views import SiteListView, SiteDetailView, SiteSummaryView, SiteSummaryAverageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sites/', SiteListView.as_view(extra_context={'nav_sites': 'active'}), name='sites'),
    path('sites/<int:pk>/', SiteDetailView.as_view(extra_context={'nav_sites': 'active'}), name='sites-detail'),
    path('summary/', SiteSummaryView.as_view(extra_context={'nav_summary': 'active'}), name='summary'),
    path('summary-average/', SiteSummaryAverageView.as_view(extra_context={'nav_summary': 'active'}), name='summary-average'),
    path('', SiteListView.as_view(), name='home')
]
