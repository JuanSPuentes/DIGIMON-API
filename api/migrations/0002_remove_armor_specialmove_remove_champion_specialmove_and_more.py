# Generated by Django 4.1.3 on 2022-11-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='armor',
            name='specialMove',
        ),
        migrations.RemoveField(
            model_name='champion',
            name='specialMove',
        ),
        migrations.RemoveField(
            model_name='hybrid',
            name='specialMove',
        ),
        migrations.RemoveField(
            model_name='mega',
            name='specialMove',
        ),
        migrations.RemoveField(
            model_name='rookie',
            name='specialMove',
        ),
        migrations.RemoveField(
            model_name='trainingi',
            name='specialMove',
        ),
        migrations.RemoveField(
            model_name='trainingii',
            name='specialMove',
        ),
        migrations.RemoveField(
            model_name='ultimate',
            name='specialMove',
        ),
        migrations.RemoveField(
            model_name='unknown',
            name='specialMove',
        ),
        migrations.RemoveField(
            model_name='xroswars',
            name='specialMove',
        ),
        migrations.AddField(
            model_name='armor',
            name='specialMove',
            field=models.ManyToManyField(blank=True, null=True, to='api.specialmove', verbose_name='SpecialMove'),
        ),
        migrations.AddField(
            model_name='champion',
            name='specialMove',
            field=models.ManyToManyField(blank=True, null=True, to='api.specialmove', verbose_name='SpecialMove'),
        ),
        migrations.AddField(
            model_name='hybrid',
            name='specialMove',
            field=models.ManyToManyField(blank=True, null=True, to='api.specialmove', verbose_name='SpecialMove'),
        ),
        migrations.AddField(
            model_name='mega',
            name='specialMove',
            field=models.ManyToManyField(blank=True, null=True, to='api.specialmove', verbose_name='SpecialMove'),
        ),
        migrations.AddField(
            model_name='rookie',
            name='specialMove',
            field=models.ManyToManyField(blank=True, null=True, to='api.specialmove', verbose_name='SpecialMove'),
        ),
        migrations.AddField(
            model_name='trainingi',
            name='specialMove',
            field=models.ManyToManyField(blank=True, null=True, to='api.specialmove', verbose_name='SpecialMove'),
        ),
        migrations.AddField(
            model_name='trainingii',
            name='specialMove',
            field=models.ManyToManyField(blank=True, null=True, to='api.specialmove', verbose_name='SpecialMove'),
        ),
        migrations.AddField(
            model_name='ultimate',
            name='specialMove',
            field=models.ManyToManyField(blank=True, null=True, to='api.specialmove', verbose_name='SpecialMove'),
        ),
        migrations.AddField(
            model_name='unknown',
            name='specialMove',
            field=models.ManyToManyField(blank=True, null=True, to='api.specialmove', verbose_name='SpecialMove'),
        ),
        migrations.AddField(
            model_name='xroswars',
            name='specialMove',
            field=models.ManyToManyField(blank=True, null=True, to='api.specialmove', verbose_name='SpecialMove'),
        ),
    ]