"""
URL configuration for brighthotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from hotelapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.openindex,name="openindex"),
    path('openabout/',views.openabout,name="openabout"),
    path('opencontact/',views.opencontact,name="opencontact"),
    path('openhome/', views.openhome, name="openhome"),
    path('opencustomer/',views.opencustomer,name="opencustomer"),
    path('customer_login/',views.customer_login,name="customer_login"),
    path('register/',views.register,name="register"),
    path('openregister/',views.openregister,name="openregister"),
    path('opencustomer_home/',views.opencustomer_home,name="opencustomer_home"),
    path('customer_logout/',views.customer_logout,name="customer_logout"),
    path('viewcontactdetails/',views.viewcontactdetails,name="viewcontactdetails"),
    path('deletecontact/<int:id>',views.deletecontact,name="deletecontact"),
    path('view_Details/',views.view_Details,name="view_Details"),
    path('change_password/',views.change_password,name="change_password"),
    path('update_profile/',views.update_profile,name="update_profile"),
    path('openadmin/',views.openadmin,name="openadmin"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path("admin_logout/",views.admin_logout,name="admin_logout"),
    path('admin_change_password/',views.admin_change_password,name="admin_change_password"),
    path('admin_view_details/',views.admin_view_details,name="admin_view_details"),
    path('deletecustomer/<int:id>',views.deletecustomer,name="deletecustomer"),
    path('admin_add_conventionhall/',views.admin_add_conventionhall,name="admin_add_conventionhall"),
    path('openadmin_add_conventionhall/', views.openadmin_add_conventionhall, name="openadmin_add_conventionhall"),
    path('admin_view_conventionhall/',views.admin_view_conventionhall,name="admin_view_conventionhall"),
    path('deleteconventionhall/<int:id>',views.deleteconventionhall,name="deleteconventionhall"),
    path('customer_view_conventionhall/',views.customer_view_conventionhall,name="customer_view_conventionhall"),

    path('rating/<int:id>',views.rating,name="rating"),
    path('edit_conventionhall/',views.edit_conventionhall,name="edit_conventionhall"),
    path('open_edit_conventionhall/<int:id>',views.open_edit_conventionhall,name="open_edit_conventionhall"),
    path('view_ratings/<int:id>',views.view_ratings,name="view_ratings"),
    path('booking/<int:id>/<int:cost>',views.booking,name="booking"),
    path('admin_view_booking/',views.admin_view_booking,name="admin_view_booking"),
    path('accept/<int:id>', views.accept, name="accept"),
    path('reject/<int:id>', views.reject, name="reject"),
    path('customer_view_booking/', views.customer_view_booking, name="customer_view_booking"),
    path('cancel/<int:id>', views.cancel, name="cancel"),
    path('admin_add_notifications/',views.admin_add_notifications,name="admin_add_notifications"),
    path('customer_view_notifications/', views.customer_view_notifications, name="customer_view_notifications"),

]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
