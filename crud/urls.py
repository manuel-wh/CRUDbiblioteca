from django.conf.urls import url
from views import EliminarFuncion, EditarFuncion, AgregarFuncion, Index, ListarClase, AgregarClase, UpdateClase, DeleteClase, ListarFuncion

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', Index, name="index"),
    url(r'^class/$', ListarClase.as_view(), name="index_clase"),
    url(r'^class/agregar$', AgregarClase.as_view(), name="agregar_clase"),
    url(r'^class/actualizar/(?P<pk>\d+)/$', UpdateClase.as_view(), name="editar_clase"),
    url(r'^class/eliminar/(?P<pk>\d+)/$', DeleteClase.as_view(), name="eliminar_clase"),
    url(r'^funcion/$', ListarFuncion, name="index_funcion"),
    url(r'^funcion/agregar$', AgregarFuncion, name="agregar_funcion"),
    url(r'^funcion/editar/(?P<id_libro>\d+)/$', EditarFuncion, name="editar_funcion"),
    url(r'^funcion/eliminar/(?P<id_libro>\d+)/$', EliminarFuncion, name="eliminar_funcion")
]
