# Generated by Django 2.0.1 on 2018-01-03 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tank', models.BooleanField(default=False)),
                ('t_shirt', models.BooleanField(default=False)),
                ('long_sleeve_shirt', models.BooleanField(default=False)),
                ('sweater', models.BooleanField(default=False)),
                ('jacket', models.BooleanField(default=False)),
                ('shorts', models.BooleanField(default=False)),
                ('jeans', models.BooleanField(default=False)),
                ('khakis', models.BooleanField(default=False)),
                ('sneakers', models.BooleanField(default=False)),
                ('boots', models.BooleanField(default=False)),
                ('flip_flops', models.BooleanField(default=False)),
                ('checkin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkin.Checkin')),
            ],
        ),
        migrations.RemoveField(
            model_name='bottom',
            name='checkin',
        ),
        migrations.RemoveField(
            model_name='shoes',
            name='checkin',
        ),
        migrations.RemoveField(
            model_name='top',
            name='checkin',
        ),
        migrations.DeleteModel(
            name='Bottom',
        ),
        migrations.DeleteModel(
            name='Shoes',
        ),
        migrations.DeleteModel(
            name='Top',
        ),
    ]