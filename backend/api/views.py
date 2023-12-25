import random

from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MoveModel, RoundModel
from .serializers import MoveSerializer, RoundStatsSerializer, UserStatsSerializer


class Round(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        '''
        Return last move of user
        '''
        last_move = MoveModel.objects.filter(user=request.user).last()
        serializer = MoveSerializer(last_move)

        return Response(serializer.data)

    def post(self, request):
        '''
        Start new move of user and return results of move
        '''
        round = RoundModel.objects.get_or_create(is_active=True)[0]

        history = list(round.history.values_list("value", flat=True))

        variants = set(range(1, 10)).difference(history)

        try:
            value = random.choice(list(variants))

            move = MoveModel(user=request.user, round=round, value=value)

        except IndexError:
            round.is_active = False

            move = MoveModel(user=request.user, round=round, value=None, jackpot=True)
            round.is_active = False

        move.save()
        round.save()

        serializer = MoveSerializer(move)

        return Response(serializer.data)


class RoundsStats(ListAPIView):
    '''
        Return statistics of rounds
    '''
    permission_classes = [permissions.IsAdminUser]

    queryset = RoundModel.objects.all().prefetch_related("history").order_by("id")
    serializer_class = RoundStatsSerializer


class UserStats(ListAPIView):
    '''
        Return statistics of users games
    '''
    permission_classes = [permissions.IsAdminUser]

    queryset = User.objects.all().prefetch_related("moves").order_by("id")
    serializer_class = UserStatsSerializer
