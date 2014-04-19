# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20140419_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='list',
            field=models.ForeignKey(to_field='id', to='lists.Item', default=None),
        ),
    ]
