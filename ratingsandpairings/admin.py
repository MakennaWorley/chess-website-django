from django.contrib import admin
from .models import UserClub, Player, Class, Game, UserGroupPlayer

admin.site.site_header = "Chess Website Superuser View"


class UserClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'key', 'owner')
    search_fields = ('name', 'key')
    list_filter = ('owner',)


admin.site.register(UserClub, UserClubAdmin)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'status', 'current_rating')
    search_fields = ('first_name', 'last_name')
    list_filter = ('status',)


admin.site.register(Player, PlayerAdmin)


class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'teacher_main', 'teacher_secondary', 'club')
    search_fields = ('name', 'level')
    list_filter = ('level', 'club')


admin.site.register(Class, ClassAdmin)


class GameAdmin(admin.ModelAdmin):
    list_display = ('board_letter', 'board_number', 'white_player', 'black_player', 'result')
    search_fields = ('board_letter', 'board_number')
    list_filter = ('result',)


admin.site.register(Game, GameAdmin)


class UserGroupPlayerAdmin(admin.ModelAdmin):
    list_display = ('club', 'player')
    search_fields = ('club__name', 'player__first_name', 'player__last_name')
    list_filter = ('club',)


admin.site.register(UserGroupPlayer, UserGroupPlayerAdmin)
