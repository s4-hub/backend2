from django.urls import path

from .views import ListRencanaView, BuatRencanaView

urlpatterns = [
    path('list-jadwal', ListRencanaView.as_view()),
    path('buat-jadwal', BuatRencanaView.as_view())
]
