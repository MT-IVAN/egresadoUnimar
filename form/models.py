from django.db import models
from .choices import *
# Create your models here.


class Degrees(models.Model):
    nivel_educacion_formal = models.CharField(max_length=16, choices=NIVEL_EDUCACION_FORMAL, blank=True, null=True)
    titulo_obtenido = models.CharField(max_length=100)
    institucion = models.CharField(max_length=200)
    anioGraduacion = models.DateField()
    def __str__(self):
        return self.nombre


class Persona(models.Model):
    ###### campos no editables
    identificacion = models.CharField(primary_key=True, max_length=12)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fechaNacimiento = models.DateField() 
    
    genero = models.CharField(max_length=10, choices=GENERO)
    programa = models.CharField(max_length=100)
    fechaGrado = models.DateField()
    ###### campos no editables
    
    ###### campos editables para el usuario

    #### 1 INFORMACION PERSONAl
    
    estado_civil = models.CharField(max_length=12, choices=ESTADO_CIVIL, blank=True, null=True)
    direccionResidencia = models.CharField(max_length=80, blank=True, null=True)
    ciudad = models.CharField(max_length=20, blank=True, null=True)
    departamento = models.CharField(max_length=20, blank=True, null=True)
    pais = models.CharField(max_length=40, blank=True, null=True)
    telefonoFijo = models.CharField(max_length=12, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    email1 = models.EmailField(max_length=150, blank=True, null=True)
    email2 = models.EmailField(max_length=150, blank=True, null=True)
    ####/ 1 INFORMACION PERSONAl

    #### 2 ACADEMICA - PENDIENTE
    # 
    ################################### aqui deberian agregarse con AJ4X los campos


    #### /2 ACADEMICA - PENDIENTE

    #### 3 INFORMACION LABORAL
    
    situacion_laboral_actual = models.CharField(max_length=34, choices=SITUACION_LABORAR, blank=True, null=True)
    experiencia_laboral = models.CharField(max_length=50, choices=EXPERIENCIA_LABORAL, blank=True, null=True)
    nombreEmpresaTrabajoActual = models.CharField(max_length=100, blank=True, null=True)
    sectorDeLaEmpresa =  models.CharField(max_length=50, choices=SECTOR_DE_LA_EMPRESA, blank=True, null=True)
    areaDeTrabajo = models.CharField(max_length=50, choices=AREA_DE_TRABAJO, blank=True, null=True)
    cargoQueOcupa =  models.CharField(max_length=50, choices=CARGO_OCUPADO, blank=True, null=True)
    nombreJefeInmediato = models.CharField(max_length=100, blank=True, null=True)
    areaTrabajoAfinConSuProfesion= models.CharField(max_length=2, choices=SI_NO, blank=True, null=True)
    tipoDeContrato = models.CharField(max_length=50, choices =TIPO_CONTRATO, blank=True, null=True )
    rangoSalarial = models.CharField(max_length=26, choices =RANGO_SALARIAL, blank=True, null=True )
    #### /3 INFORMACION LABORAL







    ###### campos editables hasta aqui

    def __str__(self):
        return self.nombres

