from django.contrib import admin
from . models import Home


class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_pagina', 'titulo_pagina',
                    'subtitulo_pagina', 'publicado_pagina')
    list_display_links = ('id', 'nome_pagina')
    list_editable = ('publicado_pagina',)


admin.site.register(Home, HomeAdmin)
