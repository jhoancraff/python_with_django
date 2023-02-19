# Generated by Django 4.0.5 on 2022-07-10 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elegir', models.CharField(max_length=200)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.nombre')),
            ],
        ),
    ]