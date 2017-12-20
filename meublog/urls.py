from django.conf.urls import url
from meublog.views import home, lista, novo, atualiza, exclui

urlpatterns = [
    url(r'^$', home),
    url(r'^lista-todos/$', lista, name='lista_todos'),
    url(r'^novo/$',novo, name="novo"),
    url(r'^atualizar/(?P<id>\d+)/$',atualiza, name='atualizar'),
    url(r'^excluir/(?P<id>\d+)/$', exclui, name='excluir'),
]