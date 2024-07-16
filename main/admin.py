from django.contrib import admin
from .models import Category, Event, Player, Statistics, PlayerStatistic

class PlayerStatisticInline(admin.TabularInline):
    model = PlayerStatistic
    extra = 1
    fields = ['lap_number', 'event', 'lap_time', 'sector1_time', 'sector2_time', 'sector3_time', 'sector4_time']

class StatisticsInline(admin.TabularInline):
    model = Statistics
    extra = 1
    fields = ['event', 'category', 'points', 'lap_time']

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'event_list', 'nationality')
    readonly_fields = ('event_list',)
    inlines = [StatisticsInline, PlayerStatisticInline]
    list_filter = ('nationality',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'date_of_start', 'player_count')
    readonly_fields = ('player_count',)
    inlines = [StatisticsInline]
    list_filter = ('country',)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj and 'player_count' not in readonly_fields:  # if we are editing an existing object
            return readonly_fields + ('player_count',)
        return readonly_fields

admin.site.register(Event, EventAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Category)
