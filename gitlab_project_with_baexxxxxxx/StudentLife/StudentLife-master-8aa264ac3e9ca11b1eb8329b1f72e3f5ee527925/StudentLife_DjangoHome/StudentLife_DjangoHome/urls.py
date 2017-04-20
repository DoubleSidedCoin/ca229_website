"""tango_with_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
#from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin
from StudentLifeApp import views


urlpatterns = [
                        # Examples:
                        # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
                        # url(r'^blog/', include('blog.urls')),
                        

                        url(r'^admin/', include(admin.site.urls)),
                        url(r'^StudentLifeApp/', include('StudentLifeApp.urls')),
			url(r'^$', views.index, name='index'),
    			url(r'^about/$', views.about, name='about'),
    			url(r'^category/(?P<category_name_slug>\w+)$', views.category, name='category'),
    			url(r'^add_category/$', views.add_category, name='add_category'),
    			url(r'^category/(?P<category_name_slug>\w+)/add_page/$', views.add_page, name='add_page'),
    			url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    
                        
                         # ADD THIS NEW TUPLE!
]

