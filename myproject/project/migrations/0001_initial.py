# Generated by Django 2.1.1 on 2018-09-16 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Female_IMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_group', models.IntegerField(default=0)),
                ('gs_mean', models.IntegerField(default=0)),
                ('apfs_mean', models.IntegerField(default=0)),
                ('ads_mean', models.IntegerField(default=0)),
                ('kfs_mean', models.IntegerField(default=0)),
                ('kes_mean', models.IntegerField(default=0)),
                ('has_mean', models.IntegerField(default=0)),
                ('hers_mean', models.IntegerField(default=0)),
                ('hirs_mean', models.IntegerField(default=0)),
                ('efs_mean', models.IntegerField(default=0)),
                ('ees_mean', models.IntegerField(default=0)),
                ('sers_mean', models.IntegerField(default=0)),
                ('sirs_mean', models.IntegerField(default=0)),
                ('gs_sd', models.IntegerField(default=0)),
                ('apfs_sd', models.IntegerField(default=0)),
                ('ads_sd', models.IntegerField(default=0)),
                ('kfs_sd', models.IntegerField(default=0)),
                ('kes_sd', models.IntegerField(default=0)),
                ('has_sd', models.IntegerField(default=0)),
                ('hers_sd', models.IntegerField(default=0)),
                ('hirs_sd', models.IntegerField(default=0)),
                ('efs_sd', models.IntegerField(default=0)),
                ('ees_sd', models.IntegerField(default=0)),
                ('sers_sd', models.IntegerField(default=0)),
                ('sirs_sd', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='History_IMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=32)),
                ('age', models.IntegerField(default=0)),
                ('gs', models.IntegerField(default=0)),
                ('apfs', models.IntegerField(default=0)),
                ('ads', models.IntegerField(default=0)),
                ('kfs', models.IntegerField(default=0)),
                ('kes', models.IntegerField(default=0)),
                ('has', models.IntegerField(default=0)),
                ('hers', models.IntegerField(default=0)),
                ('hirs', models.IntegerField(default=0)),
                ('efs', models.IntegerField(default=0)),
                ('ees', models.IntegerField(default=0)),
                ('sers', models.IntegerField(default=0)),
                ('sirs', models.IntegerField(default=0)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('sex', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=32)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='history_ims',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.User'),
        ),
    ]
