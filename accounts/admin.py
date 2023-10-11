from django.contrib import admin


from .models import Account , Profesion , Enterprise

class ProfesionInline(admin.TabularInline):
    model = Account.profesiones.through
    extra = 1

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display  = ('name', 'email', 'position',)

    list_display = ('name', 'age', 'position', 'display_profesiones')

    def display_profesiones(self, obj):
        return ', '.join([profesion.profesion for profesion in obj.profesiones.all()])
    
    display_profesiones.short_description = 'Profesiones'
    
    inlines = [
        ProfesionInline,
    ]

@admin.register(Profesion)
class ProfesiontAdmin(admin.ModelAdmin):
    list_display  = ('profesion',)

@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name_enterprise',)

