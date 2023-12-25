from django.contrib import admin

from .models import MoveModel, RoundModel


@admin.register(RoundModel)
class RoundAdmin(admin.ModelAdmin):
    pass


@admin.register(MoveModel)
class MoveAdmin(admin.ModelAdmin):
    pass
