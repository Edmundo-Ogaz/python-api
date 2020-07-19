from django.urls import path
from codigoAzul import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('albergues/', views.albergue_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)