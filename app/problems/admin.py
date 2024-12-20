from django.contrib import admin
from .models import Problems, Tage, Category, Language
from .forms import ProblemsForm
from .models import  Problems, Answer, Comments, Tage, Category, Language, Algorithm
from testunit.models import Unittestproblems, Memorytime
# Register your models here.

# problems admin 
class InloneUnittestproblems(admin.TabularInline):
    model = Unittestproblems
    extra = 0

class InloneMemorytime(admin.TabularInline):
    model = Memorytime
    extra = 0
class ProblemsAdmin(admin.ModelAdmin):
    form = ProblemsForm
    inlines = [InloneUnittestproblems, InloneMemorytime]
admin.site.register(Problems, ProblemsAdmin)
admin.site.register(Answer)
admin.site.register(Comments)
admin.site.register(Category)
admin.site.register(Tage)
admin.site.register(Language)
admin.site.register(Algorithm)

