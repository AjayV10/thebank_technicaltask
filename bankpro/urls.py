"""bankpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from bankapp import views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index1),
    path('home/', views.home),
    path('index1/', views.index1),
    path('service/', views.service),
    path('loan/', views.loan),
    path('contact/', views.contact),
    path('show/', views.show),
    path('insert/', views.insert),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('store/', views.store),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/', views.logout),
    path('signup/', views.signup_views)
]
