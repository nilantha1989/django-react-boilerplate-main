# Generated by Django 3.2.5 on 2022-09-09 04:24

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
            name='AppointmentAndAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_type', models.CharField(choices=[('VIDEOASSESSMENT', 'VIDEOASSESSMENT'), ('FORMASSESSMENT', 'FORMASSESSMENT')], max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_docto', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_patine', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreateFormOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_treatment_type', models.CharField(choices=[('ONETIMEFORM', 'ONETIMEFORM'), ('SUBSCRIPTIONFORM', 'SUBSCRIPTIONFORM')], max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_doctor', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_patinet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(max_length=255)),
                ('strength', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacy_name', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_datetime', models.DateTimeField()),
                ('appoinment', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.PROTECT, to='appoinments.appointmentandavailability')),
                ('doctor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='doc_prec', to=settings.AUTH_USER_MODEL)),
                ('form_assement', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.PROTECT, to='appoinments.createformorder')),
                ('patient', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='patient_prec', to=settings.AUTH_USER_MODEL)),
                ('pharmacy', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='pharmacy_prec', to='appoinments.pharmacy')),
            ],
        ),
        migrations.CreateModel(
            name='FormAssessementQuestioner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appoinments.createformorder')),
            ],
        ),
        migrations.AddField(
            model_name='createformorder',
            name='prefered_pharmacy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appoinments.pharmacy'),
        ),
        migrations.AddField(
            model_name='appointmentandavailability',
            name='prefered_pharmacy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appoinments.pharmacy'),
        ),
        migrations.CreateModel(
            name='PrescriptionDrug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='appoinments.drug')),
                ('prescription', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='appoinments.prescription')),
            ],
            options={
                'unique_together': {('drug', 'prescription')},
            },
        ),
    ]
