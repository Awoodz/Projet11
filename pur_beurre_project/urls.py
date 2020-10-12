"""pur_beurre_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from webapp import views
import debug_toolbar

urlpatterns = [
    url(r"^$", views.IndexView.as_view(), name="index"),
    url(r"^webapp/", include("webapp.urls")),
    url(r"^userapp/", include("userapp.urls")),
    url("admin/", admin.site.urls),
    url(r"^legalmention/", views.legal_mention, name="legalmention"),
    url(r"^account/", views.account, name="account"),
    url(r"^saved_products/", views.saved_products, name="saved_products"),
    path("accounts/", include("userapp.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    url(r"^search/$", views.search, name="search"),
    url(r"^autocomplete/$", views.ProductAutocomplete.as_view(), name="autocomplete",),
    url(r"^search_help/$", views.SearchHelpView.as_view(), name="search_help"),
    url(r"^product/(?P<product_id>[0-9]+)/$", views.product, name="product"),
    url(r"^save_product/$", views.save_product, name="save_product"),
]

urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls)),] + urlpatterns
