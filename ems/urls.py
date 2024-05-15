"""
URL configuration for ems project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import *

from account.views import *
from hr.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),

    path('login/', login_page, name='login'),
    path('logout/', logout_url, name='logout'),

    path('dashboard/', dashboard, name='dashboard'),
    path('employees/', employees, name='employees'),
    path('add-employee/', add_employee, name='add-employee'),

    path('book/<int:id>/', book, name='book'),
    path('free/<int:id>/', free, name='free'),
    path('assist/<int:id>/', assist, name='assist'),

    path('leaves/', leaves, name='leaves'),
    path('apply-leave/', apply_leave, name='apply-leave'),
    path('delete-leave/', delete_leave, name='delete-leave'),
    path('approve-leave-manager/', approve_leave_manager, name='approve-leave-manager'),
]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)