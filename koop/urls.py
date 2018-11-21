"""koop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from portal.views import StartView, AddKoopView, EditKoopView, KoopListView, KoopInfoView, \
    SupplierListView, SupplierAddView, SupplierInfoView, AddCategoryView, AddProductView, CategoryInfoView, \
    AddCustomUserView, UserListView, LoginView, UserInfoView, UserEditView, LogoutView, OrderView, OrderAddView,\
    OrderViewView, ForumView



urlpatterns = [
    path('admin/', admin.site.urls),
    url('start/', StartView.as_view(), name="start"),
  #  url('add_user/', AddUserView.as_view(), name="add_user"),
    url('add_koop/', AddKoopView.as_view(), name="add_koop"),
    url(r'^koop/edit/(?P<pk>(\d)+)/', EditKoopView.as_view(), name="edit_koop"),
    url('koop_list/', KoopListView.as_view(), name="list_koop"),
    url(r'^koop_info/(?P<id>(\d)+)/', KoopInfoView.as_view(), name="info_koop"),
    url('supplier_list/', SupplierListView.as_view(), name="supplier_list"),
    url('supplier_add/', SupplierAddView.as_view(), name="supplier_add"),
    url(r'^supplier_info/(?P<id>(\d)+)/', SupplierInfoView.as_view(), name="supplier_info"),
    url('category_add/', AddCategoryView.as_view(), name="category_add"),
    url('product_add/', AddProductView.as_view(), name="product_add"),
    url(r'^category_info/(?P<slug>([A-Za-z0-9._])+)/', CategoryInfoView.as_view(), name="category_info"),
    url('register/', AddCustomUserView.as_view(), name="register"),
    url('user_list/', UserListView.as_view(), name="user_list"),
    url('login/', LoginView.as_view(), name="login"),
    url('logout/', LogoutView.as_view(), name="logout"),
    url('user_info/', UserInfoView.as_view(), name="user_info"),
    url('user_edit/', UserEditView.as_view(), name="user_edit"),
    url('order/', OrderView.as_view(), name='order'),
    url('order_add/', OrderAddView.as_view(), name='order_add'),
    url('order_view/', OrderViewView.as_view(), name='order_view'),
    url('forum/', ForumView.as_view(), name='forum'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
