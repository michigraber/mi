from django.contrib import admin


from mi.mimamato.models import MediaUrl

class MediaUrlAdmin(admin.ModelAdmin):

    class Meta:
        abstract = True

    list_display = ('title', 'type', 'location', 'url',)


admin.site.register(MediaUrl, MediaUrlAdmin)