from django.contrib import admin

from personal.models import Movie
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class untAdmin(UserAdmin):
     list_display = ('username','mdate')
     #wat can be searched
     search_fields = ('username','mdate')
     #what cant be changed

     filter_horizontal = ()
     list_filter = ()
     fieldsets = ()

admin.site.register(Movie, untAdmin)