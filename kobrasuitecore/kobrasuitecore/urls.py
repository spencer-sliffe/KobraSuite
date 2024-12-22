"""
URL configuration for kobrasuitecore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.db import router
from django.urls import path, include

from kobrasuitecore.api.router import customer_router, school_router, work_router, investing_router, homelife_router, \
    finances_router, notifications_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(customer_router.urls)),
    path('api/', include(school_router.urls)),
    path('api/', include(work_router.urls)),
    path('api/', include(investing_router.urls)),
    path('api/', include(homelife_router.urls)),
    path('api/', include(finances_router.urls)),
    path('api/', include(notifications_router.urls)),
]
