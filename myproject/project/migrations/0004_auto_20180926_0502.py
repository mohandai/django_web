# Generated by Django 2.1.1 on 2018-09-26 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20180925_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='history_jf',
            name='ne',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='history_jf',
            name='ne_eval',
            field=models.CharField(choices=[('Weak', 'Weak'), ('Normal', 'Normal'), ('Strong', 'Strong')], default='Weak', max_length=32),
        ),
        migrations.AddField(
            model_name='history_jf',
            name='nf',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='history_jf',
            name='nf_eval',
            field=models.CharField(choices=[('Weak', 'Weak'), ('Normal', 'Normal'), ('Strong', 'Strong')], default='Weak', max_length=32),
        ),
        migrations.AddField(
            model_name='jf',
            name='ne_mean',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jf',
            name='ne_sd',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jf',
            name='nf_mean',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jf',
            name='nf_sd',
            field=models.IntegerField(default=0),
        ),
    ]