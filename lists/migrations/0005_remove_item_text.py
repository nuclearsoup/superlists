# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20140419_0732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='text',
        ),
    ]
