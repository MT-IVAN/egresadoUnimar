from django.shortcuts import render, redirect
from django.forms import modelformset_factory, inlineformset_factory
from .forms import PersonaFormInformacionPersona, DegreesForm
from .models import Persona, Degrees
# Create your views here.

def informacionPersonal(request):
    persona = Persona.objects.get(pk= 1)
    form = PersonaFormInformacionPersona(instance=persona)    
    degreeForm = DegreesForm    
    print(persona.fechaGrado)
    #preguntar acerca de la instacia
    
    #print(form.fechaGrado)

    return render(request, 'formulario/informacionPersonal.html', {'form':form, 'degreeForm':degreeForm})
#     if request.method == "POST":
#         formset = DegreeFormset(request.POST, instance=persona)    
#         if formset.is_valid():
#              formset.save()
#              return redirect('index', person_id=person_id)

#     formset = DegreeFormset(instance=persona)  
#     return render(request, 'formulario/index.html', {'formset': formset})



def login(request):
        return render(request, 'login/login.html')


def nav(request):
        return render(request, 'base/navbar.html')

