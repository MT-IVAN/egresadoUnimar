from django.shortcuts import render, redirect
from django.forms import modelformset_factory, inlineformset_factory
from .forms import PersonaFormInformacionPersona, DegreesForm, ReconocimientosForm, ParticipacionesForm, PublicacionesForm
from .models import User, Degrees, Reconocimientos, Participaciones, Publicaciones
from django.urls import reverse

import json
from django.http import HttpResponse
# Create your views here.

def informacionPersonal(request):
    persona = User.objects.get(identificacion=1) 
    if request.method == "POST": 
        print('llego la peticion por post')
        form = PersonaFormInformacionPersona(request.POST , instance=persona) 
        print('tiene el form')  
        if form.is_valid():
            print('el form es valido')  
            form.save()
            return render(request, 'formulario/informacionPersonal.html',{'form':form})
        return render(request, 'formulario/fail.html',{'form':form})
    else:
        print('llego la peticion por get')
        #necesito saber que informacion ha ingresado la persona
        form = PersonaFormInformacionPersona(instance=persona)    
        #informacion asociada a personas 
        degreesPersona = Degrees.objects.filter(persona_identificacion = 1)
        comunidadesPersona = Participaciones.objects.filter(id= 1) 
        reconocimientosPersona = Reconocimientos.objects.filter(persona_identificacion = 1)  
        publicacionesPersona = Publicaciones.objects.filter(persona_identificacion = 1)
        #envio el formulario    
        degreeForm = DegreesForm 
        reconocimietosForm = ReconocimientosForm
        participacionesForm = ParticipacionesForm    
        publicacionesForm = PublicacionesForm 
        formComunidades = ParticipacionesForm
        #return render(request, 'formulario/informacionPersonal.html', {'form':form,'degreeForm':degreeForm})
        return render(request, 'formulario/informacionPersonal.html', {'form':form,
                                                                    'degreeForm':degreeForm,
                                                                    'reconocimietosForm':reconocimietosForm,
                                                                    'participacionesForm':participacionesForm,
                                                                    'publicacionesForm':publicacionesForm,
                                                                    'titulosPersona':degreesPersona,
                                                                    'titulosComunidades':comunidadesPersona,
                                                                    'reconocimientosPersona':reconocimientosPersona,
                                                                    'publicacionesPersona':publicacionesPersona})
   
   



def ajaxGrado(request):
    if request.method == 'POST' and request.is_ajax():
            try:
                name = 'ad';
                id_titulo_obtenido = request.POST.get('id_titulo_obtenido')
                id_institucion = request.POST.get('id_institucion')
                id_anioGraduacion = request.POST.get('id_anioGraduacion')
                id_nivel_educacion_formal = request.POST.get('id_nivel_educacion_formal')

                persona = User.objects.get(identificacion=1)
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

