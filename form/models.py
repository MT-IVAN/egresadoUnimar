from django.db import models
from .choices import *
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
# Create your models here.

now = datetime.datetime.now()

# from django.contrib.auth.models import ( AbstractBaseUser, BaseUserManager)

# class UserManager(BaseUserManager):
#     def create_superuser(self,identificacion,fechaNacimiento,password=None):
#         user = self.create_user(
#             identificacion,
#             fechaNacimiento,
#             is_staff=True,
#             is_admin=True
#         )
#         return user

class Egresado(models.Model):
    ###### campos no editables
    identificacion = models.CharField(primary_key=True, max_length=12)
    nombres = models.CharField(max_length=51)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    fechaNacimiento = models.DateField(blank=True, null=True) 
    # objects = UserManager()
    # USERNAME_FIELD = 'identificacion'
    # REQUIRED_FIELDS = ['fechaNacimiento']
    
    
    genero = models.CharField(max_length=10, choices=GENERO)
    programa = models.CharField(max_length=100)
    fechaGrado = models.DateField(blank=True, null=True)
    ###### campos no editables
    
    ###### campos editables para el usuario


    #### 1 INFORMACION PERSONAl
    
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL, blank=True, null=True)
    direccionResidencia = models.CharField(max_length=80, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    departamento = models.CharField(max_length=50, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    telefonoFijo = models.IntegerField(max_length=12, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    email1 = models.EmailField(max_length=150, blank=True, null=True)
    email2 = models.EmailField(max_length=150, blank=True, null=True)
    situacion_laboral_actual = models.CharField(max_length=100, choices=SITUACION_LABORAR, blank=True, null=True)
    experiencia_laboral = models.CharField(max_length=60, choices=EXPERIENCIA_LABORAL, blank=True, null=True)
    ####/ 1 INFORMACION PERSONAl

    #### 2 ACADEMICA - PENDIENTE
    # 
    ################################### aqui deberian agregarse con AJ4X los campos


    #### /2 ACADEMICA - PENDIENTE


   
    ##### 7 

    participacionActividadesUnimar = models.CharField(max_length = 100, choices=PARTICIPACION_ACTIVIDADES, blank=True, null=True)
    serviciosDeInteres = models.CharField(max_length = 41,  blank=True, null=True)

    ###### 8 
    
    procesoDeInformacionUnimar = models.CharField(max_length=100, choices=SATISFACCION, blank=True, null=True )


    ################ otros
    # otroSectorEmpresa = models.CharField(max_length=100, blank=True, null=True)
    # otraAreaDetrabajo = models.CharField(max_length=100, blank=True, null=True)
    # otroCargo = models.CharField(max_length=100, blank=True, null=True)
    # otroServicio = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.nombres

class Degrees(models.Model):
    nivel_educacion_formal = models.CharField(max_length=100, choices=NIVEL_EDUCACION_FORMAL, blank=True, null=True)
    titulo_obtenido = models.CharField(max_length=100,null=True, blank=True,)
    institucion = models.CharField(max_length=200,null=True, blank=True)
    anioGraduacion = models.PositiveIntegerField(validators=[MinValueValidator(now.year-80),MaxValueValidator(now.year)])
    persona_identificacion = models.ForeignKey(Egresado, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo_obtenido

class Participaciones(models.Model):
    tipoDeComunidad = models.CharField(max_length = 100, choices=TIPO_COMUNIDAD_O_ASOCIACION, blank=True, null=True)
    nombreDeLaComunidad = models.CharField(max_length = 100, blank=True, null=True)
    ambitoParticipacion = models.CharField(max_length = 100, choices=AMBITO, blank=True, null=True)
    persona_identificacion = models.ForeignKey(Egresado, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreDeLaComunidad

class Reconocimientos(models.Model):
    titulo_obtenido_reconocimiento = models.CharField(max_length=100,blank=True, null=True)
    institucionReconocimiento = models.CharField(max_length=200,blank=True, null=True)
    anioReconocimiento = models.DateField(blank=True, null=True)
    ambito = models.CharField(max_length = 100, choices=AMBITO, blank=True, null=True)
    persona_identificacion = models.ForeignKey(Egresado, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo_obtenido_reconocimiento

class Publicaciones(models.Model):
    titulo_publicacion = models.CharField(max_length=100,blank=True, null=True)
    anio = models.DateField(blank=True, null=True)
    tipo_publicacion = models.CharField(max_length = 100, choices=TIPO_PUBLICACION, blank=True, null=True)
    persona_identificacion = models.ForeignKey(Egresado, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo_publicacion



#### 3 INFORMACION LABORAL
class InfoLaboral(models.Model):
    fechaInicio = models.DateField(blank=True, null=True)
    fechaFin = models.DateField(blank=True, null=True)
    nombreEmpresaTrabajoActual = models.CharField(max_length=100, blank=True, null=True)
    sectorDeLaEmpresa =  models.CharField(max_length=100, blank=True, null=True)
    areaDeTrabajo = models.CharField(max_length=100, blank=True, null=True)
    cargoQueOcupa =  models.CharField(max_length=100, blank=True, null=True)
    nombreJefeInmediato = models.CharField(max_length=100, blank=True, null=True)
    areaTrabajoAfinConSuProfesion= models.CharField(max_length=2, choices=SI_NO, blank=True, null=True)
    tipoDeContrato = models.CharField(max_length=100, choices=TIPO_CONTRATO, blank=True, null=True )
    rangoSalarial = models.CharField(max_length=100, choices=RANGO_SALARIAL, blank=True, null=True )
    checkTrabajoActual = models.CharField(max_length=2, choices=SI_NO, blank=True, null=True)
    persona_identificacion = models.ForeignKey(Egresado, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreEmpresaTrabajoActual
        
