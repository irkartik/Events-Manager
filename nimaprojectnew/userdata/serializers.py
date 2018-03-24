from .models import Appointment, Eligibility, AppliedUser
from rest_framework import serializers


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id','url', 'branch', 'full_name', 'address', 'telephone_no', 'mobile_no', 'email', 'purpose_of_visit', 'evidence_of_id', 'evidence_of_id_number', 'appointment', 'date', 'time', 'message', 'created_date')


class EligibilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eligibility
        fields = ('id', 'url', 'branch', 'name', 'email', 'address', 'phone', 'qualification', 'ielts', 'toefl', 'sat', 'gre', 'gmat', 'pte', 'priority_country', 'remarks', 'created_date')


class AppliedUserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = AppliedUser
		fields = ('id', 'url', 'branch', 'year', 'intake', 'course', 'permanent_country', 'title', 'last_name', 'middle_name', 'first_name', 'date_of_birth', 'place_of_birth', 'sex', 'nationality', 'marital_status', 'citizenship_number', 'passport_number', 'date_of_issue', 'date_of_expiry', 'place_of_issue', 'street_name_number', 'city', 'state', 'country', 'phone', 'mobile', 'email', 'is_permanent', 'school_name', 'school_city', 'school_state', 'school_country', 'school_qualification_obtained', 'school_marks_obtained', 'school_date_of_completion', 'high_school_name', 'high_school_city', 'high_school_state', 'high_school_country', 'high_school_qualification_obtained', 'high_school_marks_obtained', 'high_school_date_of_completion', 'undergrad_university', 'undergrad_city', 'undergrad_state', 'undergrad_country', 'undergrad_degree_obtained', 'undergrad_major_subject', 'undergrad_marks_obtained', 'undergrad_date_of_completion', 'graduate_university', 'graduate_city', 'graduate_state', 'graduate_country', 'graduate_degree_obtained', 'graduate_major_subject', 'graduate_marks_obtained', 'graduate_date_of_completion', 'ielts', 'toefl', 'sat', 'gre', 'gmat', 'pte', 'employment_current_employer', 'field_of_activity', 'position', 'start_date', 'department', 'employment_type', 'responsibilites', 'previous_employer', 'previous_location', 'previous_job_title', 'previous_start_date', 'previous_end_date', 'previous_employment_type', 'question1', 'question2', 'question3', 'question4', 'question5', 'question6', 'question7', 'question8', 'statement_of_purpose', 'photograph', 'resume', 'passport_copy', 'citizenship_copy', 'school_education_certificate', 'high_school_certificate', 'undergrad_certificate', 'graduate_certificate', 'test', 'certification', 'signature_name', 'date_of_signature', )