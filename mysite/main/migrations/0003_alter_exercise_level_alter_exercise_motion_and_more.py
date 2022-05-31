# Generated by Django 4.0.4 on 2022-05-31 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_exercise_equip_exercise_muscle_exercise_risk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='level',
            field=models.CharField(choices=[('beginner', 'beginner'), ('average', 'average'), ('intermediate', 'intermediate'), ('athlete', 'athlete')], default='beginner', max_length=12),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='motion',
            field=models.CharField(choices=[('static', 'static'), ('dynamic', 'dynamic')], default='dynamic', max_length=10),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='space',
            field=models.CharField(choices=[('minimal', 'minimal'), ('some', 'some'), ('large', 'large')], default='minimal', max_length=10),
        ),
        migrations.AlterField(
            model_name='exercise_muscle',
            name='muscle',
            field=models.CharField(choices=[('neck', 'neck'), ('shoulder', 'shoulder'), ('bicep', 'bicep'), ('forarm', 'forarm'), ('chest', 'chest'), ('core', 'core'), ('score', 'score'), ('tricep', 'tricep'), ('trap', 'trap'), ('lats', 'lats'), ('lowback', 'lowback'), ('hamstring', 'hamstring'), ('glute', 'glute'), ('calf', 'calf'), ('shin', 'shin'), ('quad', 'quad')], max_length=15),
        ),
    ]