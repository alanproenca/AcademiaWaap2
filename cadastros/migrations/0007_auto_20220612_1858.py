# Generated by Django 2.2.12 on 2022-06-12 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0006_auto_20220611_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.IntegerField(blank=True, null=True, verbose_name='Celular:'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cep',
            field=models.IntegerField(verbose_name='CEP:'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.IntegerField(default='', unique=True, verbose_name='CPF:'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numero',
            field=models.IntegerField(verbose_name='Número:'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Telefone:'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='celular',
            field=models.IntegerField(blank=True, null=True, verbose_name='Celular:'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cpf',
            field=models.IntegerField(default='', unique=True, verbose_name='CPF:'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='telefone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Telefone:'),
        ),
    ]