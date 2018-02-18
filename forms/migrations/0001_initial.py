# Generated by Django 2.0.2 on 2018-02-17 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, max_length=4, null=True)),
                ('intake', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=5)),
                ('last_name', models.CharField(max_length=10)),
                ('middle_name', models.CharField(blank=True, max_length=10, null=True)),
                ('first_name', models.CharField(max_length=10)),
                ('date_of_birth', models.CharField(max_length=10)),
                ('place_of_birth', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=50)),
                ('marital_status', models.CharField(max_length=50)),
                ('citizenship_number', models.CharField(max_length=100)),
                ('passport_number', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_issue', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_expiry', models.CharField(blank=True, max_length=100, null=True)),
                ('place_of_issue', models.CharField(blank=True, max_length=100, null=True)),
                ('signature_name', models.CharField(max_length=100)),
                ('date_of_signature', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CheckYourEligibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('phone', models.PositiveIntegerField()),
                ('qualification', models.CharField(max_length=100)),
                ('ielts', models.PositiveIntegerField()),
                ('toefl', models.PositiveIntegerField()),
                ('sat', models.PositiveIntegerField()),
                ('gre', models.PositiveIntegerField()),
                ('gmat', models.PositiveIntegerField()),
                ('pte', models.PositiveIntegerField()),
                ('priority_country', models.CharField(max_length=100)),
                ('remarks', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('school_city', models.CharField(blank=True, max_length=100, null=True)),
                ('school_state', models.CharField(blank=True, max_length=100, null=True)),
                ('school_country', models.CharField(blank=True, max_length=100, null=True)),
                ('school_qualification_obtained', models.CharField(blank=True, max_length=1000, null=True)),
                ('school_marks_obtained', models.CharField(blank=True, max_length=100, null=True)),
                ('school_date_of_completion', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('high_school_city', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_state', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_country', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_qualification_obtained', models.CharField(blank=True, max_length=1000, null=True)),
                ('high_school_marks_obtained', models.CharField(blank=True, max_length=100, null=True)),
                ('high_school_date_of_completion', models.CharField(blank=True, max_length=100, null=True)),
                ('undergrad_university', models.CharField(blank=True, max_length=1000, null=True)),
                ('undergrad_city', models.CharField(blank=True, max_length=100, null=True)),
                ('undergrad_state', models.CharField(blank=True, max_length=100, null=True)),
                ('undergrad_country', models.CharField(blank=True, max_length=100, null=True)),
                ('undergrad_degree_obtained', models.CharField(blank=True, max_length=1000, null=True)),
                ('undergrad_major_subject', models.CharField(max_length=100, null=True)),
                ('undergrad_marks_obtained', models.CharField(blank=True, max_length=100, null=True)),
                ('undergrad_date_of_completion', models.CharField(blank=True, max_length=100, null=True)),
                ('graduate_university', models.CharField(blank=True, max_length=1000, null=True)),
                ('graduate_city', models.CharField(blank=True, max_length=100, null=True)),
                ('graduate_state', models.CharField(blank=True, max_length=100, null=True)),
                ('graduate_country', models.CharField(blank=True, max_length=100, null=True)),
                ('graduate_degree_obtained', models.CharField(blank=True, max_length=1000, null=True)),
                ('graduate_major_subject', models.CharField(max_length=100, null=True)),
                ('graduate_marks_obtained', models.CharField(blank=True, max_length=100, null=True)),
                ('graduate_date_of_completion', models.CharField(blank=True, max_length=100, null=True)),
                ('applieduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.AppliedUser')),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employment_current_employer', models.CharField(blank=True, max_length=1000, null=True)),
                ('field_of_activity', models.CharField(blank=True, max_length=1000, null=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('employment_type', models.CharField(blank=True, max_length=100, null=True)),
                ('responsibilites', models.TextField()),
                ('previous_employer', models.CharField(blank=True, max_length=1000, null=True)),
                ('previous_location', models.CharField(blank=True, max_length=1000, null=True)),
                ('previous_job_title', models.CharField(blank=True, max_length=1000, null=True)),
                ('previous_start_date', models.CharField(blank=True, max_length=1000, null=True)),
                ('previous_end_date', models.CharField(blank=True, max_length=1000, null=True)),
                ('previous_employment_type', models.CharField(blank=True, max_length=100, null=True)),
                ('applieduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.AppliedUser')),
            ],
        ),
        migrations.CreateModel(
            name='FileUploads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photograph', models.ImageField(upload_to='')),
                ('resume', models.FileField(upload_to='')),
                ('passport_copy', models.FileField(blank=True, null=True, upload_to='')),
                ('citizenship_copy', models.FileField(blank=True, null=True, upload_to='')),
                ('school_education_certificate', models.FileField(blank=True, null=True, upload_to='')),
                ('high_school_certificate', models.FileField(blank=True, null=True, upload_to='')),
                ('undergrad_certificate', models.FileField(blank=True, null=True, upload_to='')),
                ('graduate_certificate', models.FileField(blank=True, null=True, upload_to='')),
                ('test', models.FileField(blank=True, null=True, upload_to='')),
                ('applieduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.AppliedUser')),
            ],
        ),
        migrations.CreateModel(
            name='MailingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name_number', models.CharField(blank=True, max_length=1000, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(max_length=100)),
                ('phone', models.PositiveIntegerField(blank=True, null=True)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('is_permanent', models.BooleanField(max_length=10)),
                ('applieduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.AppliedUser')),
            ],
        ),
        migrations.CreateModel(
            name='MakeAnAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=1000)),
                ('address', models.TextField()),
                ('telephone_no', models.PositiveIntegerField()),
                ('mobile_no', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('purpose_of_visit', models.CharField(max_length=100)),
                ('evidence_of_id', models.CharField(max_length=100)),
                ('evidence_of_id_number', models.CharField(max_length=100)),
                ('appointment', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OtherInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.CharField(blank=True, max_length=1000, null=True)),
                ('question2', models.CharField(blank=True, max_length=1000, null=True)),
                ('question3', models.CharField(blank=True, max_length=1000, null=True)),
                ('question4', models.CharField(blank=True, max_length=1000, null=True)),
                ('question5', models.CharField(blank=True, max_length=1000, null=True)),
                ('question6', models.CharField(blank=True, max_length=1000, null=True)),
                ('question7', models.CharField(blank=True, max_length=1000, null=True)),
                ('question8', models.CharField(blank=True, max_length=1000, null=True)),
                ('statement_of_purpose', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ielts', models.PositiveIntegerField(blank=True, null=True)),
                ('toefl', models.PositiveIntegerField(blank=True, null=True)),
                ('sat', models.PositiveIntegerField(blank=True, null=True)),
                ('gre', models.PositiveIntegerField(blank=True, null=True)),
                ('gmat', models.PositiveIntegerField(blank=True, null=True)),
                ('pte', models.PositiveIntegerField(blank=True, null=True)),
                ('applieduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.AppliedUser')),
            ],
        ),
    ]