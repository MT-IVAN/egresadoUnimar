from django.shortcuts import render, redirect
from django.forms import modelformset_factory, inlineformset_factory
from .forms import PersonaFormInformacionPersona, DegreesForm
from .models import Persona, Degrees

import json
from django.http import HttpResponse
# Create your views here.

def informacionPersonal(request):
    persona = Persona.objects.get(pk=1)
    form = PersonaFormInformacionPersona(instance=persona)    
    titulosPersona = Degrees.objects.filter(persona_identificacion = 1)
    degreeForm = DegreesForm    
    print(persona.fechaGrado)
    #preguntar acerca de la instacia
    
    #print(form.fechaGrado)

    return render(request, 'formulario/informacionPersonal.html', {'form':form, 'degreeForm':degreeForm, 'titulosPersona':titulosPersona})
#     if request.method == "POST":
#         formset = DegreeFormset(request.POST, instance=persona)    
#         if formset.is_valid():
#              formset.save()
#              return redirect('index', person_id=person_id)

#     formset = DegreeFormset(instance=persona)  
#     return render(request, 'formulario/index.html', {'formset': formset})



def ajaxGrado(request):
        if request.method == 'POST' and request.is_ajax():
                try:
                        name = 'ad';
                        id_titulo_obtenido = request.POST.get('id_titulo_obtenido')
                        id_institucion = request.POST.get('id_institucion')
                        id_anioGraduacion = request.POST.get('id_anioGraduacion')
                        id_nivel_educacion_formal = request.POST.get('id_nivel_educacion_formal')
                        persona = Persona.objects.get(identificacion=1)
                        myDegree = Degrees(nivel_educacion_formal = id_nivel_educacion_formal, titulo_obtenido = id_titulo_obtenido , institucion = id_institucion , anioGraduacion = id_anioGraduacion, persona_identificacion = persona)
                        myDegree.save()
                        dateDegree = myDegree.anioGraduacion
                        primary = myDegree.id
                except NameError:
                        print("hubo un error con la peticion")
                        name = 'ad';

                return HttpResponse(json.dumps({'id': primary ,   'id_titulo_obtenido': id_titulo_obtenido, 'id_institucion':id_institucion , 'id_anioGraduacion':dateDegree, 'id_nivel_educacion_formal':id_nivel_educacion_formal}), content_type="application/json")
        else :
                return render_to_response('ajax_test.html', locals())



def borraAjax(request):
        if request.method == 'POST' and request.is_ajax():
                try:
  
                        cursoId = request.POST.get('cursoId')
                        cursoEliminar = Degrees.objects.get(id=cursoId);
                        iden = cursoEliminar.id
                        cursoEliminar.delete()
                except NameError:
                        print("hubo un error con la peticion")

                return HttpResponse(json.dumps({'id': iden}), content_type="application/json")
        else :
                return render_to_response('ajax_test.html', locals())




def login(request):
        return render(request, 'login/login.html')


def nav(request):
        return render(request, 'base/navbar.html')

