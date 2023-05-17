from django.db import models


# Create your models here.
class Orientacion(models.Model):
    orientacion = models.CharField(max_length=40, verbose_name="Orientación")
    resolucion = models.CharField(max_length=10, verbose_name="N° Resolución")

    class Meta:
        verbose_name = "Orientación"
        verbose_name_plural = "Orientaciones"

    def __str__(self):
        return self.orientation


class Materias(models.Model):
    asignatura = models.CharField(max_length=40, verbose_name="Asignatura")
    horas = models.IntegerField(verbose_name="Horas Cátedra")
    orientacion = models.ForeignKey(Orientacion, on_delete=models.CASCADE, verbose_name='Orientación')
    cuatrimestre = models.CharField(max_length=4, verbose_name='Cuatrimestre')

    class Meta:
        verbose_name = "Materias"
        verbose_name_plural = "Materias"

    def __str__(self):
        return self.subject


class Campus(models.Model):
    campus = models.CharField(max_length=30, verbose_name='Sede')
    direccion = models.CharField(max_length=35, verbose_name='Dirección')
    referente = models.CharField(max_length=15, verbose_name='Referente')
    celular = models.CharField(max_length=10, verbose_name='Celular')

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"

    def __str__(self):
        return self.campus


class Comision(models.Model):
    STATUS_CHOICES = [('Activa', 'Activa'), ('Reagrupada', 'Reagrupada'), ('Cerrada', 'Cerrada'), ('Egresada', 'Egresada')]

    id_comision = models.CharField(max_length=11, primary_key=True, verbose_name='ID Comisión')
    comision = models.CharField(max_length=15, verbose_name='Comisión')
    orientacion = models.ForeignKey(Orientacion, on_delete=models.SET('Orientación Eliminada'))
    campus = models.ForeignKey(Campus, on_delete=models.SET('Sede Eliminada'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = "Comisión"
        verbose_name_plural = "Comisiones"

    def __str__(self):
        return self.commission


class Persona(models.Model):
    id_person = models.IntegerField(primary_key=True, verbose_name='ID Persona')
    dni = models.IntegerField(verbose_name="DNI")
    nombre = models.CharField(max_length=50, blank=False, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, blank=False, verbose_name="Apellido")
    nacimiento = models.DateField(verbose_name="Fecha de nacimiento", blank=False)
    genero = models.CharField(max_length=10, blank=True, null=False, verbose_name="Género")
    nacionalidad = models.CharField(max_length=12, blank=True, null=False, verbose_name="Nacionalidad")
    email = models.EmailField(max_length=254, blank=False, verbose_name="Correo electrónico")
    celular = models.IntegerField(verbose_name="Celular")

    class Meta:
        abstract = True


class Estudiante(Persona):
    comision = models.ManyToManyField(Comision)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Inscripción")
    lugar_nacimiento = models.CharField(max_length=100, verbose_name="Lugar de Nacimiento", blank=False)
    direccion = models.CharField(max_length=100, blank=True, verbose_name="Domicilio")
    barrio = models.CharField(max_length=30, blank=False, verbose_name="Localidad/Barrio")
    celular_2 = models.CharField(max_length=10, blank=True, null=False, verbose_name="Celular 2")
    estudios = models.CharField(max_length=20, verbose_name="Estudios Previos")
    materias_adeudadas = models.TextField(verbose_name="Materias Adeudadas", blank=True)
    colegio = models.CharField(max_length=50, verbose_name="Colegio")
    pais_colegio = models.CharField(max_length=12, verbose_name="País del colegio")
    provincia_colegio = models.CharField(max_length=35, verbose_name='Provincia del colegio')
    ciudad_colegio = models.CharField(max_length=30, verbose_name="Ciudad del colegio")
    turno_preferido = models.CharField(max_length=45, verbose_name='Turno de preferencia')
    campus_preferido = models.CharField(max_length=30, verbose_name='Sede de preferencia')

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

        def __str__(self):
            return f'{self.dni} - {self.last_name} {self.name}'


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
