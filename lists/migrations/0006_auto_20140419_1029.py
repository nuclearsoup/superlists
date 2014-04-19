# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_remove_item_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, to='lists.List', to_field='id'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='list',
            name='text',
        ),
        migrations.RemoveField(
            model_name='list',
            name='list',
        ),
    ]
