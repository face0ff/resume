from django.urls import include, path, re_path

from src.simpler.views import IndexView, CreateResume, UpdateResume

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateResume.as_view(), name='create'),
    path('update/<int:pk>', UpdateResume.as_view(), name='update'),
]
