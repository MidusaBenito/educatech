# Generated by Django 4.0.4 on 2022-05-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_mycourse_course_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='course_teaching',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='instructor_name',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
