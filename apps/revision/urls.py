from django.conf.urls import url

from views import index, revision_view, lista_revision, editar_revision, eliminar_revision

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', revision_view, name='revision_crear'),
    url(r'^lista$', lista_revision, name='revision_lista'),
    url(r'^editar/(?P<id_revisar>\d+)/$', editar_revision, name='revision_editar'),
    url(r'^eliminar/(?P<id_revisar>\d+)/$', eliminar_revision, name='revision_eliminar'),
]