# Generated by Django 2.2.4 on 2019-11-03 03:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AchievedLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityNarrative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('description', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=30)),
                ('narrativesGoal', models.IntegerField()),
                ('accumulatedNarratives', models.IntegerField()),
                ('isActive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='ComunaCorregimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opcapp.City')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeGender', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pin', models.CharField(max_length=10)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opcapp.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='HigherLevelEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Primaria', 'Primaria'), ('Secundaria', 'Secundaria'), ('Tecnico/Tecnologo', 'Tecnico/Tecnologo'), ('Universitaria', 'Universitaria')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='NeighborhoodVereda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('comunaCorregimiento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='opcapp.ComunaCorregimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('phoneNumber', models.CharField(blank=True, max_length=30)),
                ('achievedLevel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opcapp.AchievedLevel')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opcapp.Gender')),
                ('neighborhoodVeredaActual', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='personterritoryactual', to='opcapp.NeighborhoodVereda')),
                ('neighborhoodVeredaSource', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='personterritorysource', to='opcapp.NeighborhoodVereda')),
            ],
        ),
        migrations.CreateModel(
            name='RoleCampaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RoleUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zoneType', models.CharField(choices=[('Rural', 'Rural'), ('Urbana', 'Urbana')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opcapp.Country')),
            ],
        ),
        migrations.CreateModel(
            name='PersonCampaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievedLevel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opcapp.AchievedLevel')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opcapp.Campaign')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opcapp.Gender')),
                ('neighborhoodVeredaActual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personcampaignterritoryactual', to='opcapp.NeighborhoodVereda')),
                ('neighborhoodVeredaSource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personcampaignterritorysource', to='opcapp.NeighborhoodVereda')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opcapp.Person')),
                ('roleCampaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opcapp.RoleCampaign')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='roleUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opcapp.RoleUser'),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opcapp.Group')),
                ('personCampaign', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='opcapp.PersonCampaign')),
            ],
        ),
        migrations.AddField(
            model_name='neighborhoodvereda',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opcapp.Zone'),
        ),
        migrations.CreateModel(
            name='KeyConcept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('frequency', models.IntegerField()),
                ('activityNarrative', models.ManyToManyField(to='opcapp.ActivityNarrative')),
            ],
        ),
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('frequency', models.IntegerField()),
                ('activityNarrative', models.ManyToManyField(to='opcapp.ActivityNarrative')),
            ],
        ),
        migrations.AddField(
            model_name='comunacorregimiento',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opcapp.Zone'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opcapp.State'),
        ),
        migrations.AddField(
            model_name='activitynarrative',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opcapp.Campaign'),
        ),
        migrations.AddField(
            model_name='activitynarrative',
            name='personCampaign',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='opcapp.PersonCampaign'),
        ),
        migrations.AddField(
            model_name='achievedlevel',
            name='higherLevelEducation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opcapp.HigherLevelEducation'),
        ),
    ]