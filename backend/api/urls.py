from django.urls import path

from .views import Round, RoundsStats, UserStats

urlpatterns = [
    path('move', Round.as_view()),
    path('stats/rounds', RoundsStats.as_view()),
    path('stats/users', UserStats.as_view()),
]
