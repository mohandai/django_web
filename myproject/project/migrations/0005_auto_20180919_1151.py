# Generated by Django 2.1.1 on 2018-09-19 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20180919_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='IMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_group', models.IntegerField(default=0)),
                ('sex', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=32)),
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
        migrations.DeleteModel(
            name='Female_IMS',
        ),
    ]
