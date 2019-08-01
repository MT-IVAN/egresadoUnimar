from django import forms
from .models import *
from .choices import *

#Para usa la fecha evitando el error de hidden.
class DateInput(forms.DateInput):
    input_type = 'date'

class PersonaFormInformacionPersona(forms.ModelForm):
    # estado_civil = forms.ChoiceField(choices=ESTADO_CIVIL, widget=forms.RadioSelect())

    class Meta:
        model = Egresado


        fields = [
            #'identificacion',
            #'nombres', 
            #'apellidos',
            #'fechaNacimiento',
            'estado_civil',
            #'genero',
            #'programa',
            #'fechaGrado',
            'direccionResidencia',
            'ciudad',
            'departamento',
            'pais',
            'telefonoFijo',
            'celular',
            'email1',
            'email2',
            # # Informacion academica
           
            # Participacion en cominudades y asociaciones#
            
            ## PArte 7
            'participacionActividadesUnimar',
            'serviciosDeInteres',
            ## Parte 8
            'procesoDeInformacionUnimar',

            ## Otros 
            'otroSectorEmpresa',
            'otraAreaDetrabajo',
            'otroCargo',
            'otroServicio',
            
        ]
        labels= {
            #'identificacion': 'Identificación',
            'nombres': 'Nombres',
            'apellidos':'Apellidos',
            'fechaNacimiento':'Fecha de nacimiento',
            'estado_civil': 'Estado civil',
            'genero':'Género',
            'programa':'Programa estudiado en la Unimar',
            'fechaGrado':'Año de graduación',
            'direccionResidencia':'Dirección de residencia',
            'ciudad':'Ciudad',
            'departamento':'departamento',
            'pais':'Pais',
            'telefonoFijo':'Teléfono fijo',
            'celular':'Celular',
            'email1':'Email 1',
            'email2':'Email 2',
            # # Informacion laboral
            
            # Participacion en cominudades y asociaciones#
  
            ## PArte 7
            'participacionActividadesUnimar':'¿Participa en actividades de la facultad y/o Institución como egresado?',
            'serviciosDeInteres':'Servicios de mayor interés',
            ## Parte 8
            'procesoDeInformacionUnimar':'Considera que su proceso de formación en la Universidad fue:',
            ## OTROS
            'otroSectorEmpresa' : 'Otro sector',
            'otraAreaDetrabajo' : 'Otra área',
            'otroCargo' : 'Otro cargo',
            'otroServicio' : 'Otro servicio',

        }
        widgets= {
            #'identificacion': forms.TextInput(attrs={'class': 'form-control',  'id':'disabledTextInput', 'readonly':'readonly'}),
            'nombres': forms.TextInput(attrs={'class': 'validate', 'readonly':'readonly'}),
            'apellidos': forms.TextInput(attrs={'class': 'validate', 'readonly':'readonly'}),
            'fechaNacimiento': forms.TextInput(attrs={'class': 'validate', 'readonly':'readonly'}),
            'programa': forms.TextInput(attrs={'class': 'validate', 'readonly':'readonly'}),
            'fechaGrado': forms.TextInput(attrs={'class': 'validate', 'readonly':'readonly'}),
            'genero': forms.TextInput(attrs={'class': 'validate', 'readonly':'readonly'}),
            'direccionResidencia': forms.TextInput(attrs={'class': 'validate', 'required':'required'}),
            'ciudad': forms.TextInput(attrs={'class': 'validate','autocomplete':'off', 'list':'city'}),
            'departamento': forms.TextInput(attrs={'class': 'validate','autocomplete':'off', 'list':'dpto'}),
            'pais': forms.TextInput(attrs={'class': 'validate','autocomplete':'off', 'list':'country'}),
            'telefonoFijo': forms.TextInput(attrs={'class': 'validate'}),
            'celular': forms.TextInput(attrs={'class': 'validate'}),
            'email1': forms.EmailInput(attrs={'class': 'validate', 'required':'required'}),
            'email2': forms.EmailInput(attrs={'class': 'validate'}),
            'estado_civil': forms.Select(attrs={'class':'validate '}),
            # # Informacion academica
            
           
            # Participacion en cominudades y asociaciones#
            
            ## PArte 7
            'serviciosDeInteres':forms.Select(choices=SERVICIOS_DE_INTERES, attrs={'class':'validate dropdown'}),
            'participacionActividadesUnimar':forms.Select(attrs={'class':'validate dropdown'}),
            ## Parte 8
            'procesoDeInformacionUnimar':forms.Select(attrs={'class':'validate dropdown'}),

            ## otros
            'otroSectorEmpresa' : forms.TextInput(attrs={'class': 'validate', "placeholder":"Otro sector", 'id':"otroSector"}),
            'otraAreaDetrabajo' : forms.TextInput(attrs={'class': 'validate', "placeholder":"Otra área  de trabajo", 'id':"otraArea"}),
            'otroCargo' : forms.TextInput(attrs={'class': 'validate', "placeholder":"Otro cargo", 'id':"otroCargo"}),
            'otroServicio' : forms.TextInput(attrs={'class': 'validate', "placeholder":"Otros intereses", 'id':"fade2"}),


           # 'genero': forms.Select(attrs={'class':'extra-widget extra-widget-dropdown'}),
            
        }

class InfoLaboralForm(forms.ModelForm):
    class Meta:
        model = InfoLaboral
        
        fields = [
            'situacion_laboral_actual',
            'experiencia_laboral',
            'nombreEmpresaTrabajoActual',
            'sectorDeLaEmpresa',
            'areaDeTrabajo',
            'cargoQueOcupa',
            'nombreJefeInmediato',
            'areaTrabajoAfinConSuProfesion',
            'tipoDeContrato',
            'rangoSalarial',
            
        ]
        labels= {
            'situacion_laboral_actual': 'Situación laboral actual',
            'experiencia_laboral': 'Experiencia laboral',
            'nombreEmpresaTrabajoActual': 'Nombre de la empresa donde labora',
            'sectorDeLaEmpresa' : 'Sector de la empresa',
            'areaDeTrabajo' :'Área de trabajo',
            'cargoQueOcupa': 'Cargo que ocupa',
            'nombreJefeInmediato' : 'Nombre del jefe inmediato',
            'areaTrabajoAfinConSuProfesion':'¿El área de trabajo es afín a su profesión?',
            'tipoDeContrato':'Tipo de contrato',
            'rangoSalarial': 'Rango de salario',
        }
        widgets= {
            'situacion_laboral_actual':forms.Select(attrs={'class':' dropdown   validate'}),
            'experiencia_laboral': forms.Select(attrs={'class':'validate dropdown'}),
            'nombreEmpresaTrabajoActual': forms.TextInput(attrs={'class': 'validate'}),
            'sectorDeLaEmpresa' : forms.Select(attrs={'class':'validate dropdown'}),
            'areaDeTrabajo' :forms.Select(attrs={'class':'validate dropdown'}),
            'cargoQueOcupa': forms.Select(attrs={'class':'validate dropdown'}),
            'nombreJefeInmediato' : forms.TextInput(attrs={'class': 'validate'}),
            'areaTrabajoAfinConSuProfesion':forms.Select(attrs={'class':'validate dropdown'}),
            'tipoDeContrato':forms.Select(attrs={'class':'validate dropdown'}),
            'rangoSalarial': forms.Select(attrs={'class':'dropdown    validate'}),
        }


class DegreesForm(forms.ModelForm):
     
    
    class Meta:
        model = Degrees
        
        fields = [
            'nivel_educacion_formal',
            'titulo_obtenido', 
            'institucion',
            'anioGraduacion',
            
        ]
        labels= {
            'titulo_obtenido': 'Título obtenido',
            'institucion':'Institución',
            'anioGraduacion':'Año de graduación',
            'nivel_educacion_formal':'Nivel alcanzado en educación formal',
        }
        widgets= {
             'titulo_obtenido': forms.TextInput(attrs={'class': 'validate'}), 
             'institucion': forms.TextInput(attrs={'class': 'validate', 'list':'universidades'}), 
             'anioGraduacion': DateInput(attrs={'class': 'validate'}),
             'nivel_educacion_formal': forms.Select(attrs={'class':'validate dropdown'}),
        }
        

# myform.fields['status'].widget.attrs['disabled'] = True
class ParticipacionesForm(forms.ModelForm):
    class Meta:
        model = Participaciones
        
        fields = [
            'tipoDeComunidad', 
            'nombreDeLaComunidad',
            'ambitoParticipacion',
        ]
        labels= {
            'tipoDeComunidad': 'Tipo de comunidad',
            'nombreDeLaComunidad':'Nombre de la comunidad',
            'ambitoParticipacion':'Ámbito',
            
        }
        widgets= {
             'tipoDeComunidad': forms.Select(attrs={'class':'validate dropdown'}),
             'nombreDeLaComunidad': forms.TextInput(attrs={'class': 'validate'}), 
             'ambitoParticipacion':  forms.Select(attrs={'class':'validate dropdown'}),
             
        }


class ReconocimientosForm(forms.ModelForm):
    class Meta:
        model = Reconocimientos

        fields = [
            'titulo_obtenido_reconocimiento', 
            'institucionReconocimiento',
            'anioReconocimiento',
            'ambito',     
        ]
        labels= {
            'titulo_obtenido_reconocimiento': 'Nombre del reconocimiento',
            'institucionReconocimiento':'Institución otorgante',
            'anioReconocimiento':'Fecha',
            'ambito':'Ámbito',
        }
        widgets= {
            'titulo_obtenido_reconocimiento': forms.TextInput(attrs={'class': 'validate'}), 
            'institucionReconocimiento': forms.TextInput(attrs={'class': 'validate', 'list':'universidades'}), 
            'ambito': forms.Select(attrs={'class':'validate dropdown'}),
            'anioReconocimiento': DateInput(attrs={'class': 'validate'}),
        }

      

class PublicacionesForm(forms.ModelForm):
    class Meta:
        model = Publicaciones

        fields = [
            'tipo_publicacion', 
            'titulo_publicacion', 
            'anio',
             
        ]
        labels= {
            'titulo_publicacion': 'Título de la publicación',
            'anio': 'Fecha de publicación',
            'tipo_publicacion': 'Tipo de publicación', 
        }
        widgets= {
            'titulo_publicacion': forms.TextInput(attrs={'class': 'validate'}), 
            'anio': DateInput(attrs={'class': 'validate'}),
            'tipo_publicacion': forms.Select(attrs={'class':'validate dropdown'}),
        }

