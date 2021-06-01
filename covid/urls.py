from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('covid-centers/', views.centers, name="centers"),
    path('covid-tracker/', views.tracker, name="tracker"),
    path('covid-safety/', views.safety, name="safety"),
    path('tips/', views.tips, name="tips"),
    path('about/', views.about, name="about"),
    path('login/', views.login, name="login"),
    path('covid-centers/hathras/', views.hathras, name="hathras"),
    path('covid-centers/mathura/', views.mathura, name="mathura"),
    path('covid-centers/aligarh/', views.aligarh, name="aligarh"),
]
