# Generated by Django 2.2.3 on 2019-07-29 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Egresado',
            fields=[
                ('identificacion', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=51)),
                ('apellidos', models.CharField(blank=True, max_length=50, null=True)),
                ('fechaNacimiento', models.DateField(blank=True, null=True)),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=10)),
                ('programa', models.CharField(max_length=100)),
                ('fechaGrado', models.DateField(blank=True, null=True)),
                ('estado_civil', models.CharField(blank=True, choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Unión Libre', 'Unión Libre'), ('Divorciado', 'Divorciado'), ('Viudo', 'Viudo')], max_length=20, null=True)),
                ('direccionResidencia', models.CharField(blank=True, max_length=80, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=50, null=True)),
                ('departamento', models.CharField(blank=True, max_length=50, null=True)),
                ('pais', models.CharField(blank=True, max_length=50, null=True)),
                ('telefonoFijo', models.CharField(blank=True, max_length=12, null=True)),
                ('celular', models.CharField(blank=True, max_length=15, null=True)),
                ('email1', models.EmailField(blank=True, max_length=150, null=True)),
                ('email2', models.EmailField(blank=True, max_length=150, null=True)),
                ('situacion_laboral_actual', models.CharField(blank=True, choices=[('Empleado', 'Empleado'), ('Desempleado', 'Desempleado'), ('Profesional o consultor independiente', 'Profesional o consultor independiente'), ('Emprendedor/empresario', 'Emprendedor/empresario'), ('Jubilado', 'Jubilado')], max_length=100, null=True)),
                ('experiencia_laboral', models.CharField(blank=True, choices=[('Inferior a un año', 'Inferior a un año'), ('Entre 1 y 3 años', 'Entre 1 y 3 años'), ('Entre 4 y 6 años', 'Entre 4 y 6 años'), ('Entre 7 y 10 años', 'Entre 7 y 10 años'), ('Entre 11 y 15 años', 'Entre 11 y 15 años'), ('Entre 16 y 20 años', 'Entre 16 y 20 años'), ('Más de 20 años', 'Más de 20 años')], max_length=60, null=True)),
                ('nombreEmpresaTrabajoActual', models.CharField(blank=True, max_length=100, null=True)),
                ('sectorDeLaEmpresa', models.CharField(blank=True, choices=[('Agropecuario', 'Agropecuario'), ('Alimentos', 'Alimentos'), ('Asegurador', 'Asegurador'), ('Bebidas y tabaco', 'Bebidas y tabaco'), ('Comercial', 'Comercial'), ('Comunicaciones', 'Comunicaciones'), ('Construcción y obra', 'Construcción y obra'), ('Consultorías y asesorías', 'Consultorías y asesorías'), ('Consumo masivo', 'Consumo masivo'), ('Educativo', 'Educativo'), ('Energético', 'Energético'), ('Entretenimineto', 'Entretenimineto'), ('Estatal y relacionados', 'Estatal y relacionados'), ('Financiero', 'Financiero'), ('Industrial', 'Industrial'), ('Investigador', 'Investigador'), ('Manufactura', 'Manufactura'), ('Medio ambiente', 'Medio ambiente'), ('Medios', 'Medios'), ('Minería y otros materiales', 'Minería y otros materiales'), ('Publicidad y mercadeo', 'Publicidad y mercadeo'), ('Salud', 'Salud'), ('Servicios', 'Servicios'), ('Solidario', 'Solidario'), ('Técnologia', 'Técnologia'), ('Telecomunicaciones', 'Telecomunicaciones'), ('Textiles, prendas de vestir y calzado', 'Textiles, prendas de vestir y calzado'), ('Transporte', 'Transporte'), ('Turismo', 'Turismo'), ('Vehículos y partes', 'Vehículos y partes'), ('Otro', 'Otro')], max_length=100, null=True)),
                ('areaDeTrabajo', models.CharField(blank=True, choices=[('Administrativa y financiera', 'Administrativa y financiera'), ('Agronomía', 'Agronomía'), ('Audio y video/industria musical', 'Audio y video/industria musical'), ('Auditoria/contraloría/interventoría', 'Auditoria/contraloría/interventoría'), ('Calidad (aseguramiento, gestión y afines)', 'Calidad (aseguramiento, gestión y afines)'), ('Capacitación', 'Capacitación'), ('Cartera/facturación', 'Cartera/facturación'), ('Comercio exterior/logística internacional', 'Comercio exterior/logística internacional'), ('Compras', 'Compras'), ('Comunicación', 'Comunicación'), ('Construcción y obra', 'Construcción y obra'), ('Consultoria', 'Consultoria'), ('Contabilidad', 'Contabilidad'), ('Costos y presupuestos', 'Costos y presupuestos'), ('Crédito y cobranza', 'Crédito y cobranza'), ('Desarrollo productivo', 'Desarrollo productivo'), ('Desarrollo social/inclusión', 'Desarrollo social/inclusión'), ('Dirección/gerencia general/presidencia', 'Dirección/gerencia general/presidencia'), ('Diseño y publicidad', 'Diseño y publicidad'), ('Educación', 'Educación'), ('Facturación', 'Facturación'), ('Financiera', 'Financiera'), ('Hotelería y turismo', 'Hotelería y turismo'), ('Interventoría', 'Interventoría'), ('Investigación', 'Investigación'), ('Jurídica', 'Jurídica'), ('Logística y distribución', 'Logística y distribución'), ('Mantenimiento', 'Mantenimiento'), ('Medio ambiente y recursos naturales', 'Medio ambiente y recursos naturales'), ('Medios digitales', 'Medios digitales'), ('Movilidad y espacio público', 'Movilidad y espacio público'), ('Mercadeo y publicidad', 'Mercadeo y publicidad'), ('Operaciones y procesos', 'Operaciones y procesos'), ('Planeación y proyectos', 'Planeación y proyectos'), ('Producción, planta y calidad', 'Producción, planta y calidad'), ('Proyectos (análisis, desarrollo, gestión y afines)', 'Proyectos (análisis, desarrollo, gestión y afines)'), ('Psicología', 'Psicología'), ('Recreación y deporte', 'Recreación y deporte'), ('Recursos humanos y administración de personal', 'Recursos humanos y administración de personal'), ('Relaciones públicas, eventos', 'Relaciones públicas, eventos'), ('Salud/salud ocupacional', 'Salud/salud ocupacional'), ('Seguridad industrial y riesgos', 'Seguridad industrial y riesgos'), ('Servicio al cliente', 'Servicio al cliente'), ('Sistemas de sonido', 'Sistemas de sonido'), ('Sistemas de sonido', 'Sistemas de sonido'), ('Tecnología', 'Tecnología'), ('Tesorería', 'Tesorería'), ('Trabajo social', 'Trabajo social'), ('Ventas', 'Ventas'), ('Otro', 'Otro')], max_length=100, null=True)),
                ('cargoQueOcupa', models.CharField(blank=True, choices=[('Abogado', 'Abogado'), ('Administrador', 'Administrador'), ('Analista', 'Analista'), ('Arquitecto', 'Arquitecto'), ('Asesor', 'Asesor'), ('Asistente', 'Asistente'), ('Auditor', 'Auditor'), ('Auxiliar', 'Auxiliar'), ('Cajero', 'Cajero'), ('Capacitador', 'Capacitador'), ('Consultor', 'Consultor'), ('Contador', 'Contador'), ('Contralor', 'Contralor'), ('Coordinador', 'Coordinador'), ('Decano', 'Decano'), ('Dibujante', 'Dibujante'), ('Director', 'Director'), ('Diseñador', 'Diseñador'), ('Docente', 'Docente'), ('Ejecutivo', 'Ejecutivo'), ('Entrenador', 'Entrenador'), ('Especialista', 'Especialista'), ('Gerente/presidente', 'Gerente/presidente'), ('Ingeniero', 'Ingeniero'), ('Instructor', 'Instructor'), ('Investigador', 'Investigador'), ('Jefe', 'Jefe'), ('Negociador', 'Negociador'), ('Notario', 'Notario'), ('Productor', 'Productor'), ('Profesional', 'Profesional'), ('Programador', 'Programador'), ('Propietario', 'Propietario'), ('Psicólogo', 'Psicólogo'), ('Rector', 'Rector'), ('Revisor', 'Revisor'), ('Secretario', 'Secretario'), ('Subdirector', 'Subdirector'), ('Subgerente', 'Subgerente'), ('Supervisor', 'Supervisor'), ('Vicepresidente', 'Vicepresidente'), ('Vicerrector', 'Vicerrector'), ('Otro', 'Otro')], max_length=100, null=True)),
                ('nombreJefeInmediato', models.CharField(blank=True, max_length=100, null=True)),
                ('areaTrabajoAfinConSuProfesion', models.CharField(blank=True, choices=[('Sí', 'Sí'), ('No', 'No')], max_length=2, null=True)),
                ('tipoDeContrato', models.CharField(blank=True, choices=[('Término fijo', 'Término fijo'), ('Término indefinido', 'Término indefinido'), ('Prestación de servicios', 'Prestación de servicios'), ('Por obra o labor', 'Por obra o labor')], max_length=100, null=True)),
                ('rangoSalarial', models.CharField(blank=True, choices=[('Menos de $1.500.000', 'Menos de $1.500.000'), ('$1.500.000 a $2.000.000', '$1.500.000 a $2.000.000'), ('$2.000.000 a $2.500.000', '$2.000.000 a $2.500.000'), ('$2.500.000 a $3.000.000', '$2.500.000 a $3.000.000'), ('$3.000.000 a $3.500.000', '$3.000.000 a $3.500.000'), ('$3.500.000 a $4.000.000', '$3.500.000 a $4.000.000'), ('$4.000.000 a $4.500.000', '$4.000.000 a $4.500.000'), ('$4.500.000 a $5.000.000', '$4.500.000 a $5.000.000'), ('$5.000.000 a $5.500.000', '$5.000.000 a $5.500.000'), ('$5.500.000 a $6.000.000', '$5.500.000 a $6.000.000'), ('$6.000.000 a $8.000.000', '$6.000.000 a $8.000.000'), ('Más de $8.000.000', 'Más de $8.000.000')], max_length=100, null=True)),
                ('participacionActividadesUnimar', models.CharField(blank=True, choices=[('Frecuentemente', 'Frecuentemente'), ('Regularmente', 'Regularmente'), ('Eventualmente', 'Eventualmente'), ('Nunca', 'Nunca')], max_length=100, null=True)),
                ('serviciosDeInteres', models.CharField(blank=True, max_length=40, null=True)),
                ('procesoDeInformacionUnimar', models.CharField(blank=True, choices=[('Muy satisfactorio', 'Muy satisfactorio'), ('Satisfactorio', 'Satisfactorio'), ('Poco Satisfactorio', 'Poco Satisfactorio')], max_length=100, null=True)),
                ('otroSectorEmpresa', models.CharField(blank=True, max_length=100, null=True)),
                ('otraAreaDetrabajo', models.CharField(blank=True, max_length=100, null=True)),
                ('otroCargo', models.CharField(blank=True, max_length=100, null=True)),
                ('otroServicio', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reconocimientos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_obtenido_reconocimiento', models.CharField(blank=True, max_length=100, null=True)),
                ('institucionReconocimiento', models.CharField(blank=True, max_length=200, null=True)),
                ('anioReconocimiento', models.DateField(blank=True, null=True)),
                ('ambito', models.CharField(blank=True, choices=[('Local', 'Local'), ('Regional', 'Regional'), ('Nacional', 'Nacional'), ('Internacional', 'Internacional')], max_length=100, null=True)),
                ('persona_identificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='form.Egresado')),
            ],
        ),
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_publicacion', models.CharField(blank=True, max_length=100, null=True)),
                ('anio', models.DateField(blank=True, null=True)),
                ('tipo_publicacion', models.CharField(blank=True, choices=[('Artículo', 'Artículo'), ('Libro', 'Libro'), ('Capítulo de libro', 'Capítulo de libro'), ('Documento resultado de investigación', 'Documento resultado de investigación')], max_length=100, null=True)),
                ('persona_identificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='form.Egresado')),
            ],
        ),
        migrations.CreateModel(
            name='Participaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoDeComunidad', models.CharField(blank=True, choices=[('Académica', 'Académica'), ('Profesional', 'Profesional'), ('Científica', 'Científica'), ('Artística / cultural', 'Artística / cultural'), ('Deportiva', 'Deportiva')], max_length=100, null=True)),
                ('nombreDeLaComunidad', models.CharField(blank=True, max_length=100, null=True)),
                ('ambitoParticipacion', models.CharField(blank=True, choices=[('Local', 'Local'), ('Regional', 'Regional'), ('Nacional', 'Nacional'), ('Internacional', 'Internacional')], max_length=100, null=True)),
                ('persona_identificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='form.Egresado')),
            ],
        ),
        migrations.CreateModel(
            name='Degrees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_educacion_formal', models.CharField(blank=True, choices=[('Pregrado', 'Pregrado'), ('Especialización', 'Especialización'), ('Maestría', 'Maestría'), ('Doctorado', 'Doctorado')], max_length=100, null=True)),
                ('titulo_obtenido', models.CharField(blank=True, max_length=100, null=True)),
                ('institucion', models.CharField(blank=True, max_length=200, null=True)),
                ('anioGraduacion', models.DateField(blank=True, null=True)),
                ('persona_identificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='form.Egresado')),
            ],
        ),
    ]
