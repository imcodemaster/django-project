from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin.options import ModelAdmin

# Create your models here.


Department = [
				('Science', "Science"),
				('Commerce', "Commerce"),
				('Arts', "Arts"),
				('BBA', "BBA"),
				('B.Ed', "B.Ed"),
				('M.Ed', "M.Ed")
				
		]

Course = [
				('B.Sc', "B.Sc"),
				('B.Com', "B.Com"),
				('B.A', "B.A"),
				('BBA', "BBA"),
				('MBA', "MBA"),
				('B.Ed', "B.Ed"),
				('M.Ed', "M.Ed"),
				('M.Sc' , "M.Sc"),
				('M.Com' , "M.Com"),
				('M.A' , "M.A"),
				('Course1' , "Course1"),
				('Course2' , "Course2")
				
		]

Subjects = [
				('Physics', "Physics"),
				('Chemistry', "Chemistry"),
				('Zoology', "Zoology"),
				('Statics', "Statics"),
				('Maths', "Maths"),
				('English', "English"),
				('Hindi', "Hindi"),
				('Sanskrit' , "Sanskrit"),
				('Sociology' , "Sociology"),
				
		]


Semester = [
				('1', "1"),
				('2', "2"),
				('3', "3"),
				('4', "4"),
				('5', "5"),
				('6', "6")
		]


Blood_Group = [
			('A+', "A+"),
			('A-', "A-"),
			('B+', "B+"),
			('B-', "B-"),
			('AB+', "AB+"),
			('AB- ', "AB-"),
			('O+', "O+"),
			('O- ', "O-"),
	]

gender = [
				('Male', "Male"),
				('Female', "Female"),
				('Other', "Other")
		]

Religion = [
				('Indian', "Indian")
		]

nationality = [
				('Indian', "Indian")
		]

category = [
				('General', "General"),
				('OBC', "OBC"),
				('SC', "SC"),
				('ST', "ST"),
		]

domicile = [
				('Uttarakhand', "Uttarakhand"),
				('Other State', "Other State")
		]


class Profile(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE) #user
	is_staff = models.BooleanField( null = True , blank = True) #teacher or staff or not 
	registration_id = models.CharField(max_length = 10 , help_text='Enter Registration Id' ) # student registration id
	enrollment_number = models.CharField(max_length = 10 , help_text='Enter Enrollment Number') # student enrollment number
	image = models.ImageField(default = 'default.jpg' , upload_to = 'profiles_pics' , null=True , blank=True , help_text='Upload Your Picture') # student profile pic 
	signature_image = models.ImageField( upload_to = 'sign_pics', null=True , blank=True , help_text='Upload Your signature image') # student signature pic
	aadhar_image = models.ImageField( upload_to = 'aadhar_pics' , null=True , blank=True , help_text='Upload Adahar Id Picture') # student adhar id pic
	high_school_certificate_image = models.ImageField(  upload_to = 'highschool_certificate_pics' , null=True , blank=True , help_text='Upload High School Certificate Image') #highschool certificate pics of student 
	intermediate_certificate_image = models.ImageField(  upload_to = 'intermediate_certificate_pics', null=True , blank=True , help_text='Upload Intermediate Certificate Image') # intermediate certificate of studetnt 
	college_certificate_image = models.ImageField(  upload_to = 'college_certificate_pics' , null=True , blank=True , help_text='Upload Previous College Certificate Image ** Passed Year Marksheet/ Transfer Certificate') # previus passsed exam certificate of student

	date_of_birth = models.DateField(null=True  , help_text='Enter Date Of Birth ** Format - "dd/mm/yyyy"') #Studetn DOB
	father_name = models.CharField(max_length = 30 , help_text='Enter Father Name')
	mother_name = models.CharField(max_length = 30 , help_text='Enter Mother Name')
	domicile = models.CharField(max_length = 13 , choices=domicile, null=True , blank=True , help_text='Choose Your Domicile')
	aadhar = models.CharField(max_length = 17 , help_text='Enter Aadhar Id Number' )
	gender = models.CharField(max_length = 10 , choices=gender, null=True , blank=True , help_text='Choose Your Gender')
	religion = models.CharField(max_length = 15 , choices=Religion, null=True , blank=True , help_text='Choose Your Religion')
	category = models.CharField(max_length = 15 , choices=category, null=True , blank=True , help_text='Choose Category')
	nationality = models.CharField(max_length = 15 , choices=nationality, null=True , blank=True , help_text='Proud To Say Indian')
	department = models.CharField(max_length = 15 , choices=Department , null=True , blank=True , help_text='Choose Your Department' )
	course = models.CharField( max_length = 15 , choices=Course , null=True , blank=True ,help_text='Choose Your Course')
	subjects_1 = models.CharField( max_length = 15 , choices=Subjects , null=True , blank=True , help_text='Choose Your Subject 1')
	subjects_2 = models.CharField( max_length = 15 , choices=Subjects , null=True , blank=True , help_text='Choose Your Subject 2')
	subjects_3 = models.CharField( max_length = 15 , choices=Subjects , null=True , blank=True , help_text='Choose Your Subject 3')
	subjects_4 = models.CharField( max_length = 15 , choices=Subjects , null=True , blank=True , help_text='Choose Your Subject 4 ** if you have ')
	subjects_5 = models.CharField( max_length = 15 , choices=Subjects , null=True , blank=True , help_text='Choose Your Subject 5  ** if you have')

	semester = models.CharField( max_length = 3 , choices=Semester , null=True , blank=True , help_text='Choose your Semester')
	High_school_name = models.CharField(max_length = 50, null=True, blank= True  , help_text='Enter High School Name')
	High_school_board = models.CharField(max_length = 50, null=True, blank= True , help_text='Enter High School Board' )
	High_school_marks_obtained = models.IntegerField( null=True, blank= True  , help_text='Enter High School Marks Obtained')
	High_school_total_marks = models.IntegerField( null=True, blank= True  , help_text='Enter High School Total Marks ')
	High_school_percentage = models.FloatField( null=True, blank= True , help_text='Enter High School Percentage Obtained')
	High_school_subject_1 = models.CharField(max_length = 10 , null=True, blank= True  , help_text='Enter High School Subject 1')
	High_school_subject_2 = models.CharField(max_length = 10 , null=True, blank= True , help_text='Enter High School Subject 2')
	High_school_subject_3 = models.CharField(max_length = 10 , null=True, blank= True , help_text='Enter High School Subject 3')
	High_school_subject_4 = models.CharField(max_length = 10 , null=True, blank= True , help_text='Enter High School Subject 4')
	High_school_subject_5 = models.CharField(max_length = 10 , null=True, blank= True , help_text='Enter High School Subject 5')

	Intermediate_school_name = models.CharField(max_length = 50 , null=True, blank= True , help_text='Enter Intermediate School Name')
	Intermediate_school_board = models.CharField(max_length = 50 , null=True, blank= True , help_text='Enter Intermediate School Board')
	Intermediate_school_marks_obtained = models.IntegerField( null=True, blank= True , help_text='Enter Intermediate Makrs Obtained')
	Intermediate_total_marks = models.IntegerField(null=True, blank= True , help_text='Enter Intermediate Total Marks')
	Intermediate_school_percentage = models.FloatField( null=True, blank= True , help_text='Enter Intermediate Percentage')
	Intermediate_school_subject_1 = models.CharField(max_length = 10 , null=True, blank= True , help_text='Enter High School Subject 1')
	Intermediate_school_subject_2 = models.CharField(max_length = 10 , null=True, blank= True , help_text='Enter High School Subject 2')
	Intermediate_school_subject_3 = models.CharField(max_length = 10 , null=True, blank= True , help_text='Enter High School Subject 3')
	Intermediate_school_subject_4 = models.CharField(max_length = 10 , null=True, blank= True , help_text='Enter High School Subject 4')
	Intermediate_school_subject_5 = models.CharField(max_length = 10 , null=True, blank= True , help_text='Enter High School Subject 5')
	
	College_name = models.CharField(max_length = 50 , null=True, blank= True , help_text='Enter Previous College Name')
	College_board = models.CharField(max_length = 50  , null=True, blank= True , help_text='Enter University Name')
	College_marks_obtained = models.IntegerField( null=True, blank= True , help_text='Makes Obtained in Last Exam')
	total_marks = models.IntegerField( null=True, blank= True , help_text='Enter Total Marks')
	percentage = models.FloatField( null=True, blank= True , help_text='Enter Percentage Obtained')
	Course_name = models.CharField(max_length = 30  , null=True, blank= True , help_text='Enter Course you Enrolled')
	Course_semester = models.IntegerField( null=True, blank= True , help_text='Enter Semester Your Passed')
		
	mobile = models.CharField(max_length=10, null = True , blank = True , help_text='Enter Your Mobile number')
	house_no = models.CharField(max_length = 20, null = True , blank = True , help_text='Enter House / Flat Number / Colony / Ward No. ')
	address = models.CharField(max_length = 20, null = True , blank = True , help_text='Enter Your Address Details')
	city = models.CharField(max_length = 20, null = True , blank = True , help_text='Enter Your City')
	state = models.CharField(max_length = 20, null = True , blank = True , help_text='Enter Your State')
	postal_code = models.CharField(max_length = 6 , null = True , blank = True , help_text='Enter Your Postal Code ** PIN Code')
	blood_group = models.CharField(max_length = 5 , choices = Blood_Group , null = True , blank = True , help_text='Choose Your Blood Group')
	skill =  models.CharField(max_length = 50 , null = True , blank = True , help_text='About Your Skills - Things you do greatly')




	def __str__(self):
		return f'{self.user.username} Profile'
