from django.db import models

# Create your models here.

class Salarios(models.Model):
    monto = models.IntegerField(max_length=100)
    cobro_ano = models.BooleanField(blank=False) #blanck especifica si este campo puede o no ser vacío
    pago_extra = models.BooleanField(blank=False)


class PuestoTrabajo(models.Model):
    nombre_cargo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100, null=True)
    salario_monto = models.ForeignKey(Salarios,
                                      on_delete= models.CASCADE)


class Pais(models.Model):
    nombre_pais = models.CharField(max_length=100)
    #en esta linea va llave foranea pa que no se me olvide


class Poblacion(models.Model):
    nombre_poblacion = models.CharField(max_length=200)
    pais = models.ForeignKey(Pais,
                             on_delete= models.CASCADE)
    

class Fabricas(models.Model):
    nombre_fabrica = models.CharField(max_length=100)
    direccion2 = models.CharField(max_length=100)
    codigo_postal = models.IntegerField(max_length=6)
    poblacion = models.ForeignKey(Poblacion,
                                  on_delete= models.CASCADE)    


class Empleados(models.Model):
    documento = models.IntegerField(max_length=10)
    nombre = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.CharField(max_length=100)
    puesto_trabajo = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=50)
    name_cargo = models.ForeignKey(PuestoTrabajo,
                                   on_delete= models.CASCADE)
    name_fabrica = models.ForeignKey(Fabricas,
                                     on_delete= models.CASCADE)
        


    

    


    

