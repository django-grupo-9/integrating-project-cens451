from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Orientacion(models.Model):
    id_orientacion = models.AutoField(primary_key=True, verbose_name='ID Orientación')
    orientacion = models.CharField(max_length=40, verbose_name="Orientación")
    resolucion = models.CharField(max_length=10, verbose_name="N° Resolución")
    baja = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Orientación"
        verbose_name_plural = "Orientaciones"

    def __str__(self):
        return self.orientacion

    def soft_delete(self):
        self.baja = True
        super().save()

    def restore(self):
        self.baja = False
        super().save()


class Campus(models.Model):
    # id_campus = models.AutoField(primary_key=True, verbose_name='ID Campus')
    campus = models.CharField(max_length=30, verbose_name='Sede')
    direccion = models.CharField(max_length=35, verbose_name='Dirección')
    referente = models.CharField(max_length=15, verbose_name='Referente')
    celular = models.CharField(max_length=10, verbose_name='Celular')
    baja = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"

    def __str__(self):
        return self.campus

    def soft_delete(self):
        self.baja = True
        super().save()

    def restore(self):
        self.baja = False
        super().save()


class Comision(models.Model):
    STATUS_CHOICES = [('Activa', 'Activa'), ('Reagrupada', 'Reagrupada'), ('Cerrada', 'Cerrada'), ('Egresada', 'Egresada')]

    id_comision = models.AutoField(primary_key=True, verbose_name='ID Comisión')
    comision = models.CharField(max_length=15, verbose_name='Comisión')
    orientacion = models.ForeignKey(Orientacion, on_delete=models.SET('Orientación Eliminada'))
    campus = models.ForeignKey(Campus, on_delete=models.SET('Sede Eliminada'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = "Comisión"
        verbose_name_plural = "Comisiones"

    def __str__(self):
        return self.comision


class Persona(models.Model):

    GENEROS_CHOICES = (
        ('', 'Seleccione su género'),
        ('Femenino', 'Femenino'),
        ('Masculino', 'Masculino'),
        ('Otro', 'Otro')
    )

    NACIONALIDADES_CHOICES = (
        ('', 'Seleccione su nacionalidad'),
        ('Argentina', 'Argentina'),
        ('Boliviana', 'Boliviana'),
        ('Brasileña', 'Brasileña'),
        ('Chilena', 'Chilena'),
        ('Colombiana', 'Colombiana'),
        ('Ecuatoriana', 'Ecuatoriana'),
        ('Paraguaya', 'Paraguaya'),
        ('Peruana', 'Peruana'),
        ('Uruguaya', 'Uruguaya'),
        ('Venezolana', 'Venezolana'),
        ('Otro', 'Otro')
    )

    id_person = models.AutoField(primary_key=True, verbose_name='ID Persona')
    dni = models.IntegerField(verbose_name="DNI")
    nombres = models.CharField(max_length=50, blank=False, verbose_name="Nombre")
    apellidos = models.CharField(max_length=50, blank=False, verbose_name="Apellido")
    nacimiento = models.DateField(verbose_name="Fecha de nacimiento", blank=False)
    genero = models.CharField(max_length=30, choices=GENEROS_CHOICES, blank=True, null=False, verbose_name="Género")
    nacionalidad = models.CharField(max_length=55, choices=NACIONALIDADES_CHOICES, blank=True, null=False, verbose_name="Nacionalidad")
    email = models.EmailField(max_length=255, blank=False, verbose_name="Correo electrónico")
    celular_1 = models.IntegerField(verbose_name="Celular", blank=False)

    class Meta:
        abstract = True


class Estudiante(Persona):

    BARRIOS_CHOICES = (
        ('', '---'),
        ('Avellaneda', 'Avellaneda'),
        ('Caraza', 'Caraza'),
        ('C.A.B.A', 'C.A.B.A'),
        ('Gerli', 'Gerli'),
        ('Fiorito', 'Fiorito'),
        ('Lanús Este', 'Lanús Este'),
        ('Lanús Oeste', 'Lanús Oeste'),
        ('Lomas de Zamora', 'Lomas de Zamora'),
        ('Valentín Alsina', 'Valentín Alsina'),
        ('V. Jardín', 'V. Jardín'),
        ('V. Diamante', 'V. Diamante')
    )

    ESTUDIOS_CHOICES = (
        ('', 'Seleccione maximo nivel alcanzado'),
        ('primaria completa', 'Primaria 6to o 7mo grado completo'),
        ('1ro / 6 años', '1ro secundaria común de 6 años o Técnica de 7 años'),
        ('2do / 6 años', '2do secundaria común de 6 años o Técnica de 7 años'),
        ('3ro / 6 años', '3ro secundaria común de 6 años o Técnica de 7 años'),
        ('4to / 6 años', '4to secundaria común de 6 años o Técnica de 7 años'),
        ('5to / 6 años', '5to secundaria común de 6 años o Técnica de 7 años'),
        ('6to / 6 años', '6to secundaria común de 6 años o Técnica de 7 años'),
        ('1ro comun o técnica', '1ro secundaria común de 5 años o Técnica de 6 años'),
        ('2do comun o técnica', '2do secundaria común de 5 años o Técnica de 6 años'),
        ('3ro comun o técnica', '3ro secundaria común de 5 años o Técnica de 6 años'),
        ('4to comun o técnica', '4to secundaria común de 5 años o Técnica de 6 años'),
        ('5to comun o técnica', '5to secundaria común de 5 años o Técnica de 6 años'),
        ('7mo', '7mo año EGB'),
        ('8vo', '8vo año EGB'),
        ('9no', '9no año EGB'),
        ('9no Adultos', '9no año/3er ciclo EGB Adultos'),
        ('1ro polimodal', '1ro polimodal'),
        ('2do polimodal', '2do polimodal'),
        ('3ro polimodal', '3ro polimodal'),
        ('1ro ESB', '1ro secundaria básica ESB'),
        ('2do ESB', '2do secundaria básica ESB'),
        ('3ro ESB', '3ro secundaria básica ESB'),
        ('1ro fines', '1ro de Plan Fines o CENS'),
        ('2do fines', '2do de Plan Fines o CENS'),
        ('3ro fines', '3ro de Plan Fines o CENS'),
        ('1ro BAOT/BAO', '1ro de BAOT/BAO'),
        ('2do BAOT/BAO', '2do de BAOT/BAO'),
        ('3ro BAOT/BAO', '3ro de BAOT/BAO'),
        ('Otro', 'Otro'),
    )

    comision = models.ManyToManyField(Comision)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha inscripción")
    domicilio = models.CharField(max_length=100, blank=True, verbose_name="Domicilio")
    barrio = models.CharField(max_length=55, choices=BARRIOS_CHOICES, blank=True, verbose_name="Localidad/Barrio")
    celular_2 = models.CharField(max_length=10, blank=True, verbose_name="Celular 2")
    estudios = models.CharField(max_length=255, choices=ESTUDIOS_CHOICES, verbose_name="Estudios previos", blank=True)
    otros_estudios = models.CharField(max_length=255, verbose_name='Otros estudios', blank=True)
    materias_adeudadas = models.TextField(verbose_name="Materias Adeudadas", blank=True)
    colegio = models.CharField(max_length=255, verbose_name="Colegio", blank=True, null=True)
    pais = models.CharField(max_length=50, verbose_name="País del colegio", blank=True)
    provincia = models.CharField(max_length=50, verbose_name='Provincia del colegio', blank=True)
    localidad = models.CharField(max_length=50, verbose_name="Ciudad del colegio", blank=True)
    turno_manana = models.BooleanField(default=False, verbose_name='Turno mañana')
    turno_tarde = models.BooleanField(default=False, verbose_name='Turno tarde')
    turno_noche = models.BooleanField(default=False, verbose_name='Turno noche')
    sede = models.CharField(max_length=55, verbose_name='Sede de preferencia', blank=True)
    ex_alumno = models.BooleanField(verbose_name='Ex Alumno', default=False)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __str__(self):
        return f'{self.dni} - {self.apellidos} {self.nombres}'


class Legajo(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name="Estudiante")
    orientacion = models.ForeignKey(Orientacion, on_delete=models.CASCADE, verbose_name="Orientación")
    libro = models.IntegerField(verbose_name="Libro")
    folio = models.IntegerField(verbose_name="Folio")
    dni_copia = models.BooleanField(verbose_name="DNI Copia")
    p_nac_copia = models.BooleanField(verbose_name="P. Nac. Copia")
    certificado = models.BooleanField(verbose_name="Certificado de estudios")
    constancia = models.BooleanField(verbose_name="Constancia")
    observaciones = models.TextField(verbose_name="Observaciones")

    class Meta:
        verbose_name = "Legajo"
        verbose_name_plural = "Legajos"


class Asignatura(models.Model):
    id_asignatura = models.AutoField(primary_key=True, verbose_name='ID Asignatura')
    asignatura = models.CharField(max_length=40, verbose_name="Asignatura")
    horas = models.IntegerField(verbose_name="Horas Cátedra")
    orientacion = models.ForeignKey(Orientacion, on_delete=models.CASCADE, verbose_name='Orientación')
    cuatrimestre = models.CharField(max_length=4, verbose_name='Cuatrimestre')
    baja = models.BooleanField(default=False)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='asignaturas', blank=True, null=False)

    class Meta:
        verbose_name = "Materias"
        verbose_name_plural = "Materias"

    def __str__(self):
        return self.asignatura

    def soft_delete(self):
        self.baja = True
        super().save()

    def restore(self):
        self.baja = False
        super().save()
