from django.db import models

class SeqNamedMixin(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50, unique=True)
    sequence = models.PositiveSmallIntegerField(verbose_name="Sequence",default=1)
    createdDatatime = models.DateTimeField(
        verbose_name="Created Datetime", auto_now_add=True)
    lastModified = models.DateTimeField(
        verbose_name="last modified", auto_now=True)
    active = models.BooleanField(verbose_name="Active",default=True)

    class Meta:
        ordering = ['-sequence']
        abstract = True

    def __str__(self):
        return self.name