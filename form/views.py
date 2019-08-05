from django.shortcuts import render, redirect
from django.forms import modelformset_factory, inlineformset_factory
from .forms import PersonaFormInformacionPersona, DegreesForm, ReconocimientosForm, ParticipacionesForm, PublicacionesForm, InfoLaboralForm
from .models import Egresado, Degrees, Reconocimientos, Participaciones, Publicaciones, InfoLaboral
from django.urls import reverse
from django.contrib import messages
from .choices import *

import json
from django.http import HttpResponse
# Create your views here.

def informacionPersonal(request):       
    persona = None
    if 'persona' in request.session:
        personaId = int(request.session["persona"])
        persona = Egresado.objects.get(identificacion=personaId)
        degreesPersona = Degrees.objects.filter(persona_identificacion = personaId)
        comunidadesPersona = Participaciones.objects.filter(persona_identificacion= personaId) 
        reconocimientosPersona = Reconocimientos.objects.filter(persona_identificacion = personaId)  
        publicacionesPersona = Publicaciones.objects.filter(persona_identificacion = personaId)
        infoLaboralPersona = InfoLaboral.objects.filter(persona_identificacion = personaId)
        #envio el formulario    
        degreeForm = DegreesForm 
        reconocimietosForm = ReconocimientosForm
        participacionesForm = ParticipacionesForm    
        publicacionesForm = PublicacionesForm 
        formComunidades = ParticipacionesForm 
        infoLaboralForm = InfoLaboralForm
        if request.method == "POST": 
            print('llego la peticion por post')
            form = PersonaFormInformacionPersona(request.POST , instance=persona) 
            if form.is_valid(): 
                form.save()
                if persona.serviciosDeInteres != 'otro':
                    persona.otroServicio = ''
                    persona.save()
                    
            else:
                return render(request, 'formulario/fail.html',{'form':form})
        else:
            print('llego la peticion por get')
            #necesito saber que informacion ha ingresado la persona
            form = PersonaFormInformacionPersona(instance=persona)    
        return render(request, 'formulario/informacionPersonal.html', {'form':form,
                                                                        'degreeForm':degreeForm,
                                                                        'reconocimietosForm':reconocimietosForm,
                                                                        'participacionesForm':participacionesForm,
                                                                        'publicacionesForm':publicacionesForm,
                                                                        'infoLaboralForm':infoLaboralForm,
                                                                        'titulosPersona':degreesPersona,
                                                                        'titulosComunidades':comunidadesPersona,
                                                                        'reconocimientosPersona':reconocimientosPersona,
                                                                        'publicacionesPersona':publicacionesPersona,
                                                                        'personaOtros': persona,
                                                                        'infoLaboral':infoLaboralPersona,
                                                                        'opcionesSectorEmpresa':SECTOR_DE_LA_EMPRESA})
    
    else:
        return render(request, 'login/login.html')


def ajaxGrado(request):
    if request.method == 'POST' and request.is_ajax():
            try:
                id_titulo_obtenido = request.POST.get('id_titulo_obtenido')
                id_institucion = request.POST.get('id_institucion')
                id_anioGraduacion = request.POST.get('id_anioGraduacion')
                id_nivel_educacion_formal = request.POST.get('id_nivel_educacion_formal')

                persona = Egresado.objects.get(identificacion=int(request.session["persona"]))
                myDegree = Degrees(nivel_educacion_formal = id_nivel_educacion_formal, titulo_obtenido = id_titulo_obtenido , institucion = id_institucion , anioGraduacion = id_anioGraduacion, persona_identificacion = persona)
                myDegree.save()
                dateDegree = myDegree.anioGraduacion
                primary = myDegree.id
            except NameError:
                print("hubo un error con la peticion")
            return HttpResponse(json.dumps({'id': primary ,   'id_titulo_obtenido': id_titulo_obtenido, 'id_institucion':id_institucion , 'id_anioGraduacion':dateDegree, 'id_nivel_educacion_formal':id_nivel_educacion_formal}), content_type="application/json")
    else :
        return render(request, 'formulario/fail.html',{'form':form})


def Participacionajax(request):
    if request.method == 'POST' and request.is_ajax():
            try:

                id_tipoDeComunidad = request.POST.get('id_tipoDeComunidad')
                id_nombreDeLaComunidad = request.POST.get('id_nombreDeLaComunidad')
                id_ambito = request.POST.get('id_ambito')

                persona = Egresado.objects.get(identificacion=int(request.session["persona"]))

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

                persona = Egresado.objects.get(identificacion=int(request.session["persona"]))

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


                persona = Egresado.objects.get(identificacion=int(request.session["persona"]))

                miPublicacion = Publicaciones(titulo_publicacion = id_titulo_publicacion , anio = id_anio  , tipo_publicacion =  id_tipo_publicacion ,persona_identificacion = persona)
                miPublicacion.save()
                primary = miPublicacion.id
            except NameError:
                print("hubo un error con la peticion")

            return HttpResponse(json.dumps({'id': primary ,   'id_titulo_publicacion': id_titulo_publicacion, 'id_anio':id_anio ,'id_tipo_publicacion':id_tipo_publicacion}), content_type="application/json")
    else :
        return render_to_response('ajax_test.html', locals())





def guardar_info_laboral(request):
    if request.method == 'POST' and request.is_ajax():
        try:
            id_nombreEmpresaTrabajoActual = request.POST.get('id_nombreEmpresaTrabajoActual')
            id_sectorDeLaEmpresa = request.POST.get('id_sectorDeLaEmpresa')
            id_areaDeTrabajo = request.POST.get('id_areaDeTrabajo')
            id_cargoQueOcupa = request.POST.get('id_cargoQueOcupa')
            id_nombreJefeInmediato = request.POST.get('id_nombreJefeInmediato')
            id_areaTrabajoAfinConSuProfesion = request.POST.get('id_areaTrabajoAfinConSuProfesion')
            id_tipoDeContrato = request.POST.get('id_tipoDeContrato')
            id_rangoSalarial = request.POST.get('id_rangoSalarial')
            id_checkTrabajoActual = request.POST.get('id_checkTrabajoActual')
            id_fechaInicio = request.POST.get('id_fechaInicio')
            id_fechaFin = request.POST.get('id_fechaFin')

            persona = Egresado.objects.get(identificacion=int(request.session["persona"]))

            miInfoLaboral = InfoLaboral(nombreEmpresaTrabajoActual = id_nombreEmpresaTrabajoActual,
                                        sectorDeLaEmpresa = id_sectorDeLaEmpresa,
                                        areaDeTrabajo = id_areaDeTrabajo,
                                        cargoQueOcupa = id_cargoQueOcupa,
                                        nombreJefeInmediato = id_nombreJefeInmediato,
                                        areaTrabajoAfinConSuProfesion = id_areaTrabajoAfinConSuProfesion,
                                        tipoDeContrato = id_tipoDeContrato,
                                        rangoSalarial = id_rangoSalarial,
                                        checkTrabajoActual = id_checkTrabajoActual,
                                        persona_identificacion = persona,
                                        fechaInicio = id_fechaInicio,
                                        fechaFin = id_fechaFin)
            print(id_checkTrabajoActual)
            if id_checkTrabajoActual == "Sí":
               InfoLaboral.objects.filter(persona_identificacion = int(request.session["persona"])).update(checkTrabajoActual='No')


            miInfoLaboral.save()
            primary = miInfoLaboral.id


            


        except NameError:
            print("hubo un error con la peticion")

        return HttpResponse(json.dumps({'id': primary , 'id_nombreEmpresaTrabajoActual' : id_nombreEmpresaTrabajoActual,
                                        'id_sectorDeLaEmpresa' : id_sectorDeLaEmpresa,
                                        'id_areaDeTrabajo' : id_areaDeTrabajo,
                                        'id_cargoQueOcupa' : id_cargoQueOcupa,
                                        'id_nombreJefeInmediato' : id_nombreJefeInmediato,
                                        'id_areaTrabajoAfinConSuProfesion' : id_areaTrabajoAfinConSuProfesion,
                                        'id_tipoDeContrato' : id_tipoDeContrato,
                                        'id_rangoSalarial' : id_rangoSalarial,
                                        'id_checkTrabajoActual' : id_checkTrabajoActual,
                                        'id_fechaInicio' : id_fechaInicio,
                                        'id_fechaFin' : id_fechaFin }), content_type="application/json")
    else:    
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

def borrar_info_laboral(request):
        if request.method == 'POST' and request.is_ajax():
                try:
                        infoLabId = request.POST.get('infoLabId')
                        infEliminar = InfoLaboral.objects.get(id=infoLabId);
                        iden = infEliminar.id
                        infEliminar.delete()
                except NameError:
                        print("hubo un error con la peticion")

                return HttpResponse(json.dumps({'id': iden}), content_type="application/json")
        else :
                return render_to_response('ajax_test.html', locals())




def login(request):
    persona = None
    if request.method == 'POST':
        print("post")
        id_persona = request.POST.get('identificacion')
        nacimiento = request.POST.get('fechaNacimiento')
        nacimientoSplit = nacimiento.split('-')
        fechaConFormato = nacimientoSplit[2]+ "/" + nacimientoSplit[1] + "/" + nacimientoSplit[0] 
        try:
            persona = Egresado.objects.get(identificacion = int(id_persona) , fechaNacimiento = nacimiento )
            request.session['persona'] = persona.identificacion
            print("se creo la sesion")
            return redirect('info_personal')
        except:
            messages.add_message(request, messages.INFO, 'Compruebe que los datos sean correctos ')
        return render(request, 'login/login.html', {'persona':persona})
    #Si la petición llega por GET    
    else:
        ##Aqui llega la peticion de eleminar la sesion, llega por GET
        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                request.session.flush()
            return redirect('login')
        else:
            if 'persona' in request.session:
                return redirect('info_personal')
            else:    
                return render(request, 'login/login.html',{
                'persona':persona
                })

def nav(request):
        return render(request, 'base/navbar.html')

