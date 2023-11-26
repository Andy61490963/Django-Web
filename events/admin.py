from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import information
from .models import Interest

from .models import wherefrom
from .models import introduction
from .models import autobiography

from .models import Licence
from .models import Licence1

from .models import Ability
from .models import Ability1

from .models import Experience
from .models import Experience1

from .models import Dream

from .models import paper
from .models import all_aboutus
from .models import Portfolio
from .models import homepost
from .models import article

#API test
from .models import MyModel

#admin.site.register(information)
admin.site.register(Interest)

@admin.register(homepost)
class homepost(admin.ModelAdmin):
    list_display = ('postname','introduction','writer','website','post_date')
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj:
            obj.introduction = mark_safe(obj.introduction.replace('\n', '<br>'))
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
        

@admin.register(information)
class informationAdmin(admin.ModelAdmin):
    #Database 選擇性預覽內容
    list_display = ('name','introduction','refresh_date')
    #Database 上下排序根據
    #ordering = ('name')
    #Database search tool
    search_fields = ('name', 'address')

@admin.register(paper)
class paper(admin.ModelAdmin):
    list_display = ('papername','papercontent','image')
    
@admin.register(all_aboutus)
class all_aboutus(admin.ModelAdmin):
    list_display = ('experience','content','image')
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj:
            obj.content = mark_safe(obj.content.replace('\n', '<br>'))
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    
@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
    list_display = ('title','content','image')
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj:
            obj.content = mark_safe(obj.content.replace('\n', '<br>'))
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    
@admin.register(article)
class article(admin.ModelAdmin):
    list_display = ('title','content','image')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj:
            obj.content = mark_safe(obj.content.replace('\n', '<br>'))
        return super().change_view(request, object_id, form_url, extra_context=extra_context)


@admin.register(wherefrom)
class wherefrom(admin.ModelAdmin):
    list_display = ('title','content','image')

    #換行用的程式片段 針對content
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj:
            obj.content = mark_safe(obj.content.replace('\n', '<br>'))
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    
@admin.register(introduction)
class introduction(admin.ModelAdmin):
    list_display = ('title','content','image')

    #換行用的程式片段 針對content
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj:
            obj.content = mark_safe(obj.content.replace('\n', '<br>'))
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    
@admin.register(autobiography)
class autobiography(admin.ModelAdmin):
    list_display = ('title','content','image')

    #換行用的程式片段 針對content
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj:
            obj.content = mark_safe(obj.content.replace('\n', '<br>'))
        return super().change_view(request, object_id, form_url, extra_context=extra_context)



@admin.register(Licence)
class Licence(admin.ModelAdmin):
    list_display = ('title','content','image')

    #換行用的程式片段 針對content
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj:
            obj.content = mark_safe(obj.content.replace('\n', '<br>'))
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    
@admin.register(Licence1)
class Licence1(admin.ModelAdmin):
    list_display = ('title','content','image')

    #換行用的程式片段 針對content
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj:
            obj.content = mark_safe(obj.content.replace('\n', '<br>'))
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    

@admin.register(Ability)
class Ability(admin.ModelAdmin):
    list_display = ('title','content','image')

    #換行用的程式片段 針對content
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj:
            obj.content = mark_safe(obj.content.replace('\n', '<br>'))
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    
@admin.register(Ability1)
class Ability1(admin.ModelAdmin):
    list_display = ('title','content','image')

    #換行用的程式片段 針對content
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj:
            obj.content = mark_safe(obj.content.replace('\n', '<br>'))
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    
@admin.register(Experience)
class Experience(admin.ModelAdmin):
    list_display = ('title','content','image')

    #換行用的程式片段 針對content
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj:
            obj.content = mark_safe(obj.content.replace('\n', '<br>'))
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    
@admin.register(Experience1)
class Experience1(admin.ModelAdmin):
    list_display = ('title','content','image')

    #換行用的程式片段 針對content
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj:
            obj.content = mark_safe(obj.content.replace('\n', '<br>'))
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    
@admin.register(Dream)
class Dream(admin.ModelAdmin):
    list_display = ('title','content','image')

    #換行用的程式片段 針對content
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj:
            obj.content = mark_safe(obj.content.replace('\n', '<br>'))
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    
@admin.register(MyModel)
class MyModel(admin.ModelAdmin):
    list_display = ('name',)

    #換行用的程式片段 針對content
    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj:
            obj.content = mark_safe(obj.content.replace('\n', '<br>'))
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
