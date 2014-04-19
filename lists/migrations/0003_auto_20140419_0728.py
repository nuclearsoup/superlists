# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='text',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='list',
            name='list',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
