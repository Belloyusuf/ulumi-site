from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('news_detail/', views.news_detail, name='news_details'),
    path('history/', views.history, name='history'),
    path('<int:year>/<int:month>/<int:day>/<slug:news>/', views.full_detail, name='full_detail'),
] 