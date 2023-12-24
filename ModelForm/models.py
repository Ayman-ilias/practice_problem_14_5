from django.db import models

# Create your models here.
class Modelss(models.Model):
    auto_field = models.AutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    duration_field = models.DurationField()
    # file_path_field = models.FilePathField(path='/path/to/files/')
    generic_ip_address_field = models.GenericIPAddressField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    json_field = models.JSONField()
    positive_big_integer_field = models.PositiveBigIntegerField()
    slug_field = models.SlugField()
    url_field = models.URLField()
    uuid_field = models.UUIDField()