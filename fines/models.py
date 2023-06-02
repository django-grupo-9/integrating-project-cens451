from django.db import models


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


class Asignatura(models.Model):
    id_asignatura = models.AutoField(primary_key=True, verbose_name='ID Asignatura')
    asignatura = models.CharField(max_length=40, verbose_name="Asignatura")
    horas = models.IntegerField(verbose_name="Horas Cátedra")
    orientacion = models.ForeignKey(Orientacion, on_delete=models.CASCADE, verbose_name='Orientación')
    cuatrimestre = models.CharField(max_length=4, verbose_name='Cuatrimestre')
    baja = models.BooleanField(default=False)

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
    id_person = models.AutoField(primary_key=True, verbose_name='ID Persona')
    dni = models.IntegerField(verbose_name="DNI")
    nombres = models.CharField(max_length=50, blank=False, verbose_name="Nombre")
    apellidos = models.CharField(max_length=50, blank=False, verbose_name="Apellido")
    nacimiento = models.DateField(verbose_name="Fecha de nacimiento", blank=False)
    genero = models.CharField(max_length=30, blank=True, null=False, verbose_name="Género")
    nacionalidad = models.CharField(max_length=55, blank=True, null=False, verbose_name="Nacionalidad")
    email = models.EmailField(max_length=255, blank=False, verbose_name="Correo electrónico")
    celular_1 = models.IntegerField(verbose_name="Celular", blank=False)

    class Meta:
        abstract = True


class Estudiante(Persona):
    comision = models.ManyToManyField(Comision)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha inscripción")
    domicilio = models.CharField(max_length=100, blank=True, verbose_name="Domicilio")
    barrio = models.CharField(max_length=55, blank=True, verbose_name="Localidad/Barrio")
    celular_2 = models.CharField(max_length=10, blank=True, verbose_name="Celular 2")
    estudios = models.CharField(max_length=255, verbose_name="Estudios previos", blank=True)
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
