from django.contrib import admin
from .models import Product, Lawyer, ImageTitle, BackgroundImage

#admin.site.register(Product)
admin.site.register(BackgroundImage)

@admin.register(Lawyer)
class LawyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')

@admin.register(ImageTitle)
class ImageTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')  # نمایش تیتر و عکس در لیست
    search_fields = ('title',)  # قابلیت جستجو بر اساس تیتر

