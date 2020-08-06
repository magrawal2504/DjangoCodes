# Generated by Django 3.1 on 2020-08-05 13:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('qwerty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countViewsDownload.journal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countViewsDownload.useragent')),
            ],
        ),
        migrations.AddField(
            model_name='journal',
            name='publicationJ',
            field=models.ManyToManyField(to='countViewsDownload.Publication'),
        ),
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ip_address', models.GenericIPAddressField()),
                ('action', models.CharField(choices=[('PV', 'Article web page view'), ('DL', 'Article download')], max_length=2)),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countViewsDownload.publication')),
                ('user_agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='countViewsDownload.useragent')),
            ],
        ),
    ]