from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Profile


class UserRegisterForm(UserCreationForm):
	
	first_name = forms.CharField(max_length = 30 , help_text='Enter First Name ** Middle Name also (if any)')
	last_name = forms.CharField(max_length = 30 , help_text='Enter Last Name')
	email = forms.EmailField(help_text='Enter Your Email to get Activate link ')
	
	

	class Meta:
		model = User
		fields = ["username", "first_name" , "last_name", "email" , "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [ 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta : 
		model = Profile
		fields = [ 'registration_id' , 'enrollment_number', 'image' ,'signature_image','aadhar_image', 'date_of_birth' , 'father_name' , 'mother_name', 'domicile' , 'aadhar' , 'gender' , 'religion', 'category' ,
		 'nationality' , 'department' , 'course' , 'subjects_1' , 'subjects_2' , 'subjects_3' , 'subjects_4' , 'subjects_5' ,'semester' ,'High_school_name' , 'High_school_board' , 'High_school_marks_obtained', 
'High_school_total_marks' ,  'High_school_percentage' , 'High_school_subject_1' , 'High_school_subject_2' ,  
	'High_school_subject_3' ,  'High_school_subject_4' ,'High_school_subject_5', 
	'high_school_certificate_image', 'Intermediate_school_name', 'Intermediate_school_board','Intermediate_school_marks_obtained',
	'Intermediate_total_marks' ,'Intermediate_school_percentage' ,'Intermediate_school_subject_1' ,
	'Intermediate_school_subject_2','Intermediate_school_subject_3', 'Intermediate_school_subject_4' , 'Intermediate_school_subject_5', 'intermediate_certificate_image' ,
	 'College_name' , 'College_board','College_marks_obtained' ,'total_marks' , 'percentage', 
	'Course_name','Course_semester', 'college_certificate_image' ,  'mobile' , 'house_no' , 'address' , 'city' ,
		 'state' , 'postal_code' , 'blood_group' , 'skill' ]

