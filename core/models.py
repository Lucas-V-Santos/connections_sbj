from django.db import models


class Base(models.Model):
    created = models.DateField('criado', auto_now=True)
    modified = models.DateField('modificado', auto_now=True)
    status = models.BooleanField('status', default=True)

    class Meta:
        abstract = True


class ConnectionModel(Base):
    DEVICE_TYPE = (
        ('D', 'desktop'),
        ('N', 'notebook'),
        ('T', 'tablet'),
        ('S', 'smartphone')
    )
    code = models.CharField('codigo', max_length=12, blank=False, null=False, unique=True)
    ip = models.CharField('ip', max_length=15, blank=True, null=True, unique=True)
    device = models.CharField('device', choices=DEVICE_TYPE, max_length=1, null=False, blank=False, default='D')
    description = models.CharField('descrição', max_length=30, blank=False, null=False)
    type = models.CharField('tipo', max_length=25)
    mac = models.CharField('mac', max_length=25, blank=True, null=True, unique=True)
    name = models.CharField('nome', max_length=60, blank=True, null=True, unique=True)


