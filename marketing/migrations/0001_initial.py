# Generated by Django 4.0.4 on 2022-05-10 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ContractType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingScope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingPartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=200)),
                ('workingPart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.workingpart')),
            ],
        ),
        migrations.AddField(
            model_name='workingpart',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.workingscope'),
        ),
        migrations.CreateModel(
            name='MarketingMeeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField()),
                ('subject', models.CharField(max_length=200)),
                ('notes', models.TextField()),
                ('status', models.CharField(choices=[('C ', 'Canceled'), ('D', 'Done'), ('P', 'Pending'), ('S', 'Shifted')], max_length=40)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.employee')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.meetingtype')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=200)),
                ('statement', models.TextField()),
                ('priceInNumber', models.FloatField()),
                ('totalArea', models.IntegerField()),
                ('totalTimePeriod', models.IntegerField()),
                ('GregorianDate', models.DateTimeField(auto_now_add=True)),
                ('contractSubject', models.TextField()),
                ('additionalDetails', models.TextField()),
                ('MunicipalConfirmed', models.BooleanField()),
                ('contractType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.contracttype')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('projectComponents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.projectcomponent')),
                ('workingScope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.workingscope')),
            ],
        ),
        migrations.CreateModel(
            name='ComponentPartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=200)),
                ('componentPart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.componentpart')),
            ],
        ),
        migrations.AddField(
            model_name='componentpart',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketing.projectcomponent'),
        ),
    ]
