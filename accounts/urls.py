from django.urls import path
from .views import index, yangi_sahifa,PageRuView,PageUzView


urlpatterns = [
    path('', index, name='index'),
    path('yangi_sahifa/<str:ism>/<str:nomer>/', yangi_sahifa, name='page'),
    path('page/ru/' ,PageRuView.as_view(), name='pageru' ),
    path('page/uz/' ,PageUzView.as_view(), name='pageuz' ),

]

