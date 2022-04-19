from django.db import models
from cloudinary import models as modelsCloudinary

# Create your models here.


class Plato(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    foto = modelsCloudinary.CloudinaryField(
        folder='plato')  # models.ImageField()
    disponible = models.BooleanField(default=True, null=False)
    precio = models.FloatField(null=False)

    class Meta:
        db_table = 'platos'


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(null=False)
    cantidad = models.IntegerField(null=False)
    precio_diario = models.FloatField(null=False)

    # Related_name => Servira para ingresar desde el modelo del cual se esta creando la relación (en este caso desde platos podremos ingresar a todos sus stocks)
    # on_delete => Qué acción tomará cuando se desee eliminar el padre (la pk)
    # CASCADE = Eliminará el registro del plato y todos los stocks que tengan ese registro tbn serán eliminado en cascada

    platoId = models.ForeignKey(
        to=Plato, related_name="stocks", on_delete=models.CASCADE, db_column='plato_id')

    class Meta:
        db_table = 'stocks'
        unique_together = ['fecha', 'platoId']
