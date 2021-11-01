from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin

from .models import *


class OuterwearAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and not instance.clothing_length:
            self.fields['trend'].widget.attrs.update({
                'readonly': True, 'style': 'background: lightgray;'
            })

    def clean(self):
        if not self.cleaned_data['clothing_length']:
            self.cleaned_data['trend'] = None
        return self.cleaned_data


class ShoesAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='shoess'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class OuterwearAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = OuterwearAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='outerwears'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class SweatshirtsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='sweatshirtss'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class CostumesAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='costumess'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class JeansAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='jeanss'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Shoes, ShoesAdmin)
admin.site.register(Outerwear, OuterwearAdmin)
admin.site.register(Sweatshirts, SweatshirtsAdmin)
admin.site.register(Jeans, JeansAdmin)
admin.site.register(Costumes, CostumesAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Review)

