from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    # /daten
    path('', views.index, name="index"),

    # /daten/hive_name
    path('<hive_name>/', views.detail, name="detail"),

    # /daten/hive_name/measure
    path('<hive_name>/measure/', views.measure, name="measure"),

]