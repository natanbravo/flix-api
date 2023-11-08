# Generated by Django 4.2.7 on 2023-11-08 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(choices=[('USA', 'Estados Unidos'), ('BRAZIL', 'Brasil'), ('PARAGUAY', 'Paraguay')], max_length=100, null=True)),
            ],
        ),
    ]
