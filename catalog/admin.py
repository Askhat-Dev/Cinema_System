from django.contrib import admin
from .models import Producer, Movie, Actor, MovieInstance,Genre
# admin.site.register(Movie)
# admin.site.register(Producer)
admin.site.register(Genre)
admin.site.register(MovieInstance)
# admin.site.register(Actor)

# Define the admin class
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

class ActorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

admin.site.register(Producer, ProducerAdmin)
admin.site.register(Actor, ActorAdmin)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'producer', 'display_genre','actor',)