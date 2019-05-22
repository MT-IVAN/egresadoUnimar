from django import forms
from .models import Persona, Degrees
from .choices import *

class PersonaFormInformacionPersona(forms.ModelForm):
    # estado_civil = forms.ChoiceField(choices=ESTADO_CIVIL, widget=forms.RadioSelect())
    class Meta:
        model = Persona


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

            
            
        }
        widgets= {
            'identificacion': forms.TextInput(attrs={'class': 'form-control',  'id':'disabledTextInput', 'disabled':'disabled'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'disabled':'disabled'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'disabled':'disabled'}),
            'fechaNacimiento': forms.TextInput(attrs={'class': 'form-control', 'disabled':'disabled'}),
            'programa': forms.TextInput(attrs={'class': 'form-control', 'disabled':'disabled'}),
            'fechaGrado': forms.TextInput(attrs={'class': 'form-control', 'disabled':'disabled'}),
            'genero': forms.TextInput(attrs={'class': 'form-control', 'disabled':'disabled'}),
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
            'anioGraduacion': forms.TextInput(attrs={'class': 'form-control'}), 
            'nivel_educacion_formal': forms.Select(attrs={'class':'extra-widget extra-widget-dropdown selectpicker form-control'}),
        }

# myform.fields['status'].widget.attrs['disabled'] = True