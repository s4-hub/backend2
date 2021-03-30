from django.urls import path

from .views import BuatRencanaView

urlpatterns = [
    path('list-jadwal', BuatRencanaView.as_view())
]
