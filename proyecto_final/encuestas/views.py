from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from encuestas.forms import FormularioRespuesta
from encuestas.models import Encuesta, Pregunta, Respuesta


def logout_view(request):
    logout(request)


class EncuestasListView(ListView, LoginRequiredMixin):
    template_name = 'encuestas/listado_encuestas.html'
    model = Encuesta
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        title_page = "Maestro | Años Base"
        main_title_content = "Años Base"
        main_subtitle_content = "List"
        subtitle_table = "Lista"

        context.update({
            'CLASS_MENU_MAESTROS': "menu-open",
            'CLASS_MENU_MAESTROS_SELECT': "active",
            'CLASS_MENU_ANIO': "menu-open",
            'CLASS_SUBMENU_ANIO': "active",
            'CLASS_SUBMENU_ANIO_LIST': "active",
            'title_page': title_page,
            'main_title_content': main_title_content,
            'main_subtitle_content': main_subtitle_content,
            'subtitle_table': subtitle_table,
        })
        return context


class PreguntaListView(TemplateView):
    template_name = 'preguntas/listado.html'
    listado = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        encuesta_id = kwargs.get('uuid_encuesta', None)
        self.listado = Pregunta.objects.filter(encuesta_id=encuesta_id)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        titulo = "Listado preguntas"
        main_title_content = "Años Base"
        
        context.update({
            'titulo': titulo,
            'main_title_content': main_title_content,
            'listado': self.listado,
        })
        return context


class RespuestaAddView(CreateView):
    template_name = 'respuestas/agregar.html'
    model = Respuesta
    form_class = FormularioRespuesta
    pregunta = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.pregunta = kwargs.get('uuid_pregunta', None)
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['pregunta'].initial = self.pregunta
        return form

    def form_valid(self, form):
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.usuario = self.request.user
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        titulo = "Agregar respuesta"
        context.update({
            'titulo': titulo,
        })
        return context
    
    def get_success_url(self):
        messages.success(self.request, 'El registro fue AGREGADO exitosamente, {}'.format(
            self.object.pregunta.pregunta))
        return reverse('pregunta_list', kwargs={'uuid_encuesta': self.object.pregunta.encuesta_id})


@method_decorator(login_required, name='dispatch')
class RespuestaEditView(UpdateView, LoginRequiredMixin):
    template_name = 'respuestas/agregar.html'
    model = Respuesta
    form_class = FormularioRespuesta

    def get_object(self, queryset=None):
        return get_object_or_404(Respuesta, id=self.kwargs.get('uuid_respuesta'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        titulo = "Editar respuesta"
        context.update({
            'titulo': titulo,
        })
        return context

    def get_success_url(self):
        messages.success(self.request, 'El registro fue AGREGADO exitosamente, {}'.format(
            self.object.pregunta.pregunta))
        return reverse('pregunta_list', kwargs={'uuid_encuesta': self.object.pregunta.encuesta_id})
