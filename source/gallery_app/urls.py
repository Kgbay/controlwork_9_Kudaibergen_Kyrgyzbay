from django.urls import path

from .views import IndexView
from .views import ImageCreateView, ImageDetail, ImageUpdateView, ImageDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("images/add/", ImageCreateView.as_view(), name='image_add'),
    path("images/<int:pk>/", ImageDetail.as_view(), name='image_view'),
    path('images/<int:pk>/update/', ImageUpdateView.as_view(), name='image_update'),
    path('images/<int:pk>/delete/', ImageDeleteView.as_view(), name='image_delete'),
    path('images/<int:pk>/confirm_delete/', ImageDeleteView.as_view(), name='confirm_delete'),
]
