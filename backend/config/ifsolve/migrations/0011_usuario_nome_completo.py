# Generated by Django 4.1.3 on 2023-01-08 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifsolve', '0010_alter_alternativa_justificativa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nome_completo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
