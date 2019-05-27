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
    degreesPersona = Degrees.objects.filter(persona_identificacion = 1)
    comunidadesPersona = Participaciones.objects.filter(persona_identificacion= 1) 
    reconocimientosPersona = Reconocimientos.objects.filter(persona_identificacion = 1)  
    publicacionesPersona = Publicaciones.objects.filter(persona_identificacion = 1)
    #envio el formulario    
    degreeForm = DegreesForm 
    reconocimietosForm = ReconocimientosForm
    participacionesForm = ParticipacionesForm    
    publicacionesForm = PublicacionesForm 
    formComunidades = ParticipacionesForm 
    if request.method == "POST": 
        print('llego la peticion por post')
        form = PersonaFormInformacionPersona(request.POST , instance=persona) 
        print('tiene el form')  
        if form.is_valid():
            print('el form es valido')  
            form.save()
            return render(request, 'formulario/informacionPersonal.html', {'form':form,
                                                                    'degreeForm':degreeForm,
                                                                    'reconocimietosForm':reconocimietosForm,
                                                                    'participacionesForm':participacionesForm,
                                                                    'publicacionesForm':publicacionesForm,
                                                                    'titulosPersona':degreesPersona,
                                                                    'titulosComunidades':comunidadesPersona,
                                                                    'reconocimientosPersona':reconocimientosPersona,
                                                                    'publicacionesPersona':publicacionesPersona})
        return render(request, 'formulario/fail.html',{'form':form})
    else:
        print('llego la peticion por get')
        #necesito saber que informacion ha ingresado la persona
        form = PersonaFormInformacionPersona(instance=persona)    
        # #informacion asociada a personas 
        # degreesPersona = Degrees.objects.filter(persona_identificacion = 1)
        # comunidadesPersona = Participaciones.objects.filter(persona_identificacion= 1) 
        # reconocimientosPersona = Reconocimientos.objects.filter(persona_identificacion = 1)  
        # publicacionesPersona = Publicaciones.objects.filter(persona_identificacion = 1)
        # #envio el formulario    
        # degreeForm = DegreesForm 
        # reconocimietosForm = ReconocimientosForm
        # participacionesForm = ParticipacionesForm    
        # publicacionesForm = PublicacionesForm 
        # formComunidades = ParticipacionesForm
        # #return render(request, 'formulario/informacionPersonal.html', {'form':form,'degreeForm':degreeForm})
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
            return HttpResponse(json.dumps({'id': primary ,   'id_titulo_obtenido': id_titulo_obtenido, 'id_institucion':id_institucion , 'id_anioGraduacion':dateDegree, 'id_nivel_educacion_formal':id_nivel_educacion_formal}), content_type="application/json")
    else :
        return render_to_response('ajax_test.html', locals())


def Participacionajax(request):
    if request.method == 'POST' and request.is_ajax():
            try:

                id_tipoDeComunidad = request.POST.get('id_tipoDeComunidad')
                id_nombreDeLaComunidad = request.POST.get('id_nombreDeLaComunidad')
                id_ambito = request.POST.get('id_ambito')

                persona = User.objects.get(identificacion=1)

                miParticipacion = Participaciones(tipoDeComunidad = id_tipoDeComunidad , nombreDeLaComunidad = id_nombreDeLaComunidad  , ambitoParticipacion = id_ambito  , persona_identificacion = persona)
                miParticipacion.save()
                primary = miParticipacion.id
            except NameError:
                print("hubo un error con la peticion")

            return HttpResponse(json.dumps({'id': primary ,   'id_tipoDeComunidad': id_tipoDeComunidad, 'id_nombreDeLaComunidad':id_nombreDeLaComunidad , 'id_ambito':id_ambito}), content_type="application/json")
    else :
        return render_to_response('ajax_test.html', locals())


def guardar_reconocimiento(request):
    if request.method == 'POST' and request.is_ajax():
            try:

                id_titulo_obtenido_reconocimiento = request.POST.get('id_titulo_obtenido_reconocimiento')
                id_institucionReconocimiento = request.POST.get('id_institucionReconocimiento')
                id_anioReconocimiento = request.POST.get('id_anioReconocimiento')
                id_ambito = request.POST.get('id_ambito')

                persona = User.objects.get(identificacion=1)

                mireconocimiento = Reconocimientos(titulo_obtenido_reconocimiento = id_titulo_obtenido_reconocimiento , institucionReconocimiento = id_institucionReconocimiento  , anioReconocimiento =  id_anioReconocimiento , ambito =id_ambito ,persona_identificacion = persona)
                mireconocimiento.save()
                primary = mireconocimiento.id
            except NameError:
                print("hubo un error con la peticion")

            return HttpResponse(json.dumps({'id': primary ,   'id_titulo_obtenido_reconocimiento': id_titulo_obtenido_reconocimiento, 'id_institucionReconocimiento':id_institucionReconocimiento ,'id_anioReconocimiento':id_anioReconocimiento, 'id_ambito':id_ambito}), content_type="application/json")
    else :
        return render_to_response('ajax_test.html', locals())



def guardar_publicacion(request):
    if request.method == 'POST' and request.is_ajax():
            try:

                id_titulo_publicacion = request.POST.get('id_titulo_publicacion')
                id_anio = request.POST.get('id_anio')
                id_tipo_publicacion = request.POST.get('id_tipo_publicacion')


                persona = User.objects.get(identificacion=1)

                miPublicacion = Publicaciones(titulo_publicacion = id_titulo_publicacion , anio = id_anio  , tipo_publicacion =  id_tipo_publicacion ,persona_identificacion = persona)
                miPublicacion.save()
                primary = miPublicacion.id
            except NameError:
                print("hubo un error con la peticion")

            return HttpResponse(json.dumps({'id': primary ,   'id_titulo_publicacion': id_titulo_publicacion, 'id_anio':id_anio ,'id_tipo_publicacion':id_tipo_publicacion}), content_type="application/json")
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



def borrar_comunidad(request):
        if request.method == 'POST' and request.is_ajax():
                try:
                        comunidadId = request.POST.get('cursoId')
                        print(comunidadId)
                        comunidadEliminar = Participaciones.objects.get(id=comunidadId);
                        iden = comunidadEliminar.id
                        comunidadEliminar.delete()
                except NameError:
                        print("hubo un error con la peticion")

                return HttpResponse(json.dumps({'id': iden}), content_type="application/json")
        else :
                return render_to_response('ajax_test.html', locals())


def borrar_reconocimiento(request):
        if request.method == 'POST' and request.is_ajax():
                try:
                        comunidadId = request.POST.get('cursoId')
                        print(comunidadId)
                        comunidadEliminar = Reconocimientos.objects.get(id=comunidadId);
                        iden = comunidadEliminar.id
                        comunidadEliminar.delete()
                except NameError:
                        print("hubo un error con la peticion")

                return HttpResponse(json.dumps({'id': iden}), content_type="application/json")
        else :
                return render_to_response('ajax_test.html', locals())

def borrar_publicacion(request):
        if request.method == 'POST' and request.is_ajax():
                try:
                        comunidadId = request.POST.get('cursoId')
                        print(comunidadId)
                        comunidadEliminar = Publicaciones.objects.get(id=comunidadId);
                        iden = comunidadEliminar.id
                        comunidadEliminar.delete()
                except NameError:
                        print("hubo un error con la peticion")

                return HttpResponse(json.dumps({'id': iden}), content_type="application/json")
        else :
                return render_to_response('ajax_test.html', locals())




def login(request):
        return render(request, 'login/login.html')


def nav(request):
        return render(request, 'base/navbar.html')

