from django.urls import path

# from . import views
from encuestas.views import *


urlpatterns = [
    path('encuestas', EncuestasListView.as_view(), name='encuesta_list'),
    path('encuestas/<str:uuid_encuesta>',
         PreguntaListView.as_view(), name='pregunta_list'),
    path('encuestas/<str:uuid_encuesta>/preguntas/<str:uuid_pregunta>',
         RespuestaAddView.as_view(), name='respuesta_add'),
    path('encuestas/<str:uuid_encuesta>/preguntas/<str:uuid_pregunta>/respuesta/<str:uuid_respuesta>',
         RespuestaEditView.as_view(), name='respuesta_edit'),
    
]
