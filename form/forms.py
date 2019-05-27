from django import forms
from .models import *
from .choices import *

#Para usa la fecha evitando el error de hidden.
class DateInput(forms.DateInput):
    input_type = 'date'

class PersonaFormInformacionPersona(forms.ModelForm):
    # estado_civil = forms.ChoiceField(choices=ESTADO_CIVIL, widget=forms.RadioSelect())

    class Meta:
        model = User


        fields = [
            'identificacion',
            'nombres', 
            'apellidos',
            'fechaNacimiento',
            'estado_civil',
            'genero',
            'programa',
            'fechaGrado',
            'direccionResidencia',
            'ciudad',
            'departamento',
            'pais',
            'telefonoFijo',
            'celular',
            'email1',
            'email2',
            # # Informacion academica
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
            # Participacion en cominudades y asociaciones#
            
            ## PArte 7
            'participacionActividadesUnimar',
            'serviciosDeInteres',
            ## Parte 8
            'procesoDeInformacionUnimar',
            
        ]
        labels= {
            'identificacion': 'Identificación',
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
            # # Informacion academica
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
            # Participacion en cominudades y asociaciones#
  
            ## PArte 7
            'participacionActividadesUnimar':'¿Participa en actividades de la facultad y/o Institución como egresado?',
            'serviciosDeInteres':'Servicios de mayor interés',
            ## Parte 8
            'procesoDeInformacionUnimar':'Considera que su proceso de formación en la Universidad fue:',
        }
        widgets= {
            'identificacion': forms.TextInput(attrs={'class': 'form-control',  'id':'disabledTextInput', 'value':'1', 'readonly':'readonly'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'readonly':'readonly'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'readonly':'readonly'}),
            'fechaNacimiento': forms.TextInput(attrs={'class': 'form-control', 'readonly':'readonly'}),
            'programa': forms.TextInput(attrs={'class': 'form-control', 'readonly':'readonly'}),
            'fechaGrado': forms.TextInput(attrs={'class': 'form-control', 'readonly':'readonly'}),
            'genero': forms.TextInput(attrs={'class': 'form-control', 'readonly':'readonly'}),
            'direccionResidencia': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'telefonoFijo': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'email1': forms.TextInput(attrs={'class': 'form-control'}),
            'email2': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker  form-control'}),
            # # Informacion academica
            'situacion_laboral_actual':forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker form-control'}),
            'experiencia_laboral': forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker  form-control'}),
            'nombreEmpresaTrabajoActual': forms.TextInput(attrs={'class': 'form-control'}),
            'sectorDeLaEmpresa' : forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker  form-control'}),
            'areaDeTrabajo' :forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker  form-control'}),
            'cargoQueOcupa': forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker  form-control'}),
            'nombreJefeInmediato' : forms.TextInput(attrs={'class': 'form-control'}),
            'areaTrabajoAfinConSuProfesion':forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker  form-control'}),
            'tipoDeContrato':forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker  form-control'}),
            'rangoSalarial': forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker  form-control'}),
           
            # Participacion en cominudades y asociaciones#
            
            ## PArte 7
            'serviciosDeInteres':forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker  form-control'}),
            'participacionActividadesUnimar':forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker  form-control'}),
            ## Parte 8
            'procesoDeInformacionUnimar':forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker  form-control'}),




           # 'genero': forms.Select(attrs={'class':'extra-widget extra-widget-dropdown'}),
            
        }


class DegreesForm(forms.ModelForm):
     
    
    class Meta:
        model = Degrees
        
        fields = [
            'titulo_obtenido', 
            'institucion',
            'anioGraduacion',
            'nivel_educacion_formal',
        ]
        labels= {
            'titulo_obtenido': 'Título obtenido',
            'institucion':'Institución',
            'anioGraduacion':'Año de graduación',
            'nivel_educacion_formal':'Nivel alcanzado en educación formal',
        }
        widgets= {
             'titulo_obtenido': forms.TextInput(attrs={'class': 'form-control'}), 
             'institucion': forms.TextInput(attrs={'class': 'form-control'}), 
             'anioGraduacion': DateInput(attrs={'class': 'form-control'}),
             'nivel_educacion_formal': forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker form-control'}),
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
             'tipoDeComunidad': forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker  form-control'}),
             'nombreDeLaComunidad': forms.TextInput(attrs={'class': 'form-control'}), 
             'ambitoParticipacion':  forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker  form-control'}),
             
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
            'titulo_obtenido_reconocimiento': forms.TextInput(attrs={'class': 'form-control'}), 
            'institucionReconocimiento': forms.TextInput(attrs={'class': 'form-control'}), 
            'ambito': forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker form-control'}),
            'anioReconocimiento': DateInput(attrs={'class': 'form-control'}),
        }

      

class PublicacionesForm(forms.ModelForm):
    class Meta:
        model = Publicaciones

        fields = [
            'titulo_publicacion', 
            'anio',
            'tipo_publicacion',  
        ]
        labels= {
            'titulo_publicacion': 'Título de la publicación',
            'anio': 'Fecha de publicación',
            'tipo_publicacion': 'Tipo de publicación', 
        }
        widgets= {
            'titulo_publicacion': forms.TextInput(attrs={'class': 'form-control'}), 
            'anio': DateInput(attrs={'class': 'form-control'}),
            'tipo_publicacion': forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker form-control'}),
        }

