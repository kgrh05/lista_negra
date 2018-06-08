from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('lista_negra', views.Lista_Negra_View)


urlpatterns = [
	url('', include(router.urls))
]

