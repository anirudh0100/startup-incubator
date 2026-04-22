from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# ✅ Common US States (used everywhere)
US_STATES = (
    ('Alabama', 'Alabama'),
    ('Alaska', 'Alaska'),
    ('Arizona', 'Arizona'),
    ('Arkansas', 'Arkansas'),
    ('California', 'California'),
    ('Colorado', 'Colorado'),
    ('Connecticut', 'Connecticut'),
    ('Delaware', 'Delaware'),
    ('Florida', 'Florida'),
    ('Georgia', 'Georgia'),
    ('Hawaii', 'Hawaii'),
    ('Idaho', 'Idaho'),
    ('Illinois', 'Illinois'),
    ('Indiana', 'Indiana'),
    ('Iowa', 'Iowa'),
    ('Kansas', 'Kansas'),
    ('Kentucky', 'Kentucky'),
    ('Louisiana', 'Louisiana'),
    ('Maine', 'Maine'),
    ('Maryland', 'Maryland'),
    ('Massachusetts', 'Massachusetts'),
    ('Michigan', 'Michigan'),
    ('Minnesota', 'Minnesota'),
    ('Mississippi', 'Mississippi'),
    ('Missouri', 'Missouri'),
    ('Montana', 'Montana'),
    ('Nebraska', 'Nebraska'),
    ('Nevada', 'Nevada'),
    ('New Hampshire', 'New Hampshire'),
    ('New Jersey', 'New Jersey'),
    ('New Mexico', 'New Mexico'),
    ('New York', 'New York'),
    ('North Carolina', 'North Carolina'),
    ('North Dakota', 'North Dakota'),
    ('Ohio', 'Ohio'),
    ('Oklahoma', 'Oklahoma'),
    ('Oregon', 'Oregon'),
    ('Pennsylvania', 'Pennsylvania'),
    ('Rhode Island', 'Rhode Island'),
    ('South Carolina', 'South Carolina'),
    ('South Dakota', 'South Dakota'),
    ('Tennessee', 'Tennessee'),
    ('Texas', 'Texas'),
    ('Utah', 'Utah'),
    ('Vermont', 'Vermont'),
    ('Virginia', 'Virginia'),
    ('Washington', 'Washington'),
    ('West Virginia', 'West Virginia'),
    ('Wisconsin', 'Wisconsin'),
    ('Wyoming', 'Wyoming'),
)

# Common Roles
ROLES_CHOICE = (
    ('Student', 'Student'),
    ('Entrepreneur', 'Entrepreneur'),
    ('Mentor', 'Mentor'),
    ('Investor', 'Investor'),
    ('Organization', 'Organization')
)


# -------------------- STUDENT --------------------
class StudentDetails(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    age = models.IntegerField()
    mobile = models.CharField(max_length=15)
    college = models.CharField(max_length=200)
    state = models.CharField(max_length=100, choices=US_STATES)
    city = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLES_CHOICE)
    interest1 = models.CharField(max_length=100)
    interest2 = models.CharField(max_length=100)
    interest3 = models.CharField(max_length=100)
    about_yourself = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'StudentDetails'


# -------------------- ENTREPRENEUR --------------------
class EntrepreneurDetails(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    age = models.IntegerField()
    mobile = models.CharField(max_length=15)
    state = models.CharField(max_length=100, choices=US_STATES)
    city = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLES_CHOICE)
    interest1 = models.CharField(max_length=100)
    interest2 = models.CharField(max_length=100)
    interest3 = models.CharField(max_length=100)
    about_yourself = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'EntrepreneurDetails'


# -------------------- INVESTOR --------------------
class InvestorDetails(models.Model):

    THEMES_CHOICE = (
        ('ARTIFICIAL INTELLIGENCE', 'ARTIFICIAL INTELLIGENCE'),
        ('SMART AUTOMATION', 'SMART AUTOMATION'),
        ('FITNESS & SPORTS', 'FITNESS & SPORTS'),
        ('HERITAGE & CULTURE', 'HERITAGE & CULTURE'),
        ('MEDTECH/BIOTECH/ HEALTHTECH', 'MEDTECH/BIOTECH/ HEALTHTECH'),
        ('SMART VEHICLES', 'SMART VEHICLES'),
        ('FINANCE', 'FINANCE'),
        ('AGRICULTURE, FOODTECH & RURAL DEVELOPMENT', 'AGRICULTURE, FOODTECH & RURAL DEVELOPMENT'),
        ('ROBOTICS AND DRONES', 'ROBOTICS AND DRONES'),
        ('TRANSPORTATION', 'TRANSPORTATION'),
        ('TOURISM', 'TOURISM'),
        ('CLEAN & GREEN TECHNOLOGY', 'CLEAN & GREEN TECHNOLOGY'),
        ('BLOCKCHAIN & CYBERSECURITY', 'BLOCKCHAIN & CYBERSECURITY'),
        ('RENEWABLE/ SUSTAINABLE ENERGY', 'RENEWABLE/ SUSTAINABLE ENERGY'),
        ('SMART EDUCATION', 'SMART EDUCATION'),
        ('DISASTER MANAGEMENT', 'DISASTER MANAGEMENT'),
        ('AERONAUTICS', 'AERONAUTICS'),
        ('MISCELLANEOUS', 'MISCELLANEOUS'),
    )

    STAGES_CHOICE = (
        ('Ideation', 'Ideation'),
        ('Validation', 'Validation'),
        ('EarlyTraction', 'EarlyTraction'),
        ('Scaling', 'Scaling'),
    )

    SECTORS_CHOICE = (
        ('Big Data', 'Big Data'),
        ('Business Intelligence', 'Business Intelligence'),
        ('Machine Learning', 'Machine Learning'),
        ('NLP', 'NLP'),
        ('Blockchain', 'Blockchain'),
        ('Pharmaceutical', 'Pharmaceutical'),
        ('Digital Media Publishing', 'Digital Media Publishing'),
        ('Foreign Exchange', 'Foreign Exchange'),
        ('Food Processing', 'Food Processing'),
        ('Healthcare Services', 'Healthcare Services'),
        ('Virtual Games', 'Virtual Games'),
        ('Trading', 'Trading'),
        ('AR/VR', 'AR/VR'),
        ('Construction Technologies', 'Construction Technologies'),
        ('Smart Home', 'Smart Home'),
        ('IoT', 'Internet of Things'),
        ('Crowdfunding', 'Crowdfunding'),
        ('P2P', 'P2P'),
        ('Finance', 'Finance'),
        ('E-commerce', 'E-commerce'),
        ('SaaS', 'SaaS'),
        ('Others', 'Others'),
    )

    mobile_number = models.CharField(max_length=12)
    landline_number = models.CharField(max_length=12, blank=True)
    website = models.URLField(blank=True, default='')
    state = models.CharField(max_length=100, choices=US_STATES)
    city = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    about = models.TextField()
    focus_industries = MultiSelectField(choices=THEMES_CHOICE)
    focus_sectors = MultiSelectField(choices=SECTORS_CHOICE)
    startup_stages = MultiSelectField(choices=STAGES_CHOICE)
    min_investment_range = models.IntegerField()
    max_investment_range = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'InvestorDetails'


# -------------------- MENTOR --------------------
class MentorDetails(models.Model):

    THEMES_CHOICE = InvestorDetails.THEMES_CHOICE
    STAGES_CHOICE = InvestorDetails.STAGES_CHOICE
    SECTORS_CHOICE = InvestorDetails.SECTORS_CHOICE

    mobile_number = models.CharField(max_length=12)
    website = models.URLField(blank=True, default='')
    state = models.CharField(max_length=100, choices=US_STATES)
    city = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    about = models.TextField()
    focus_industries = MultiSelectField(choices=THEMES_CHOICE)
    guidance_areas = MultiSelectField(choices=SECTORS_CHOICE)
    startup_stages = MultiSelectField(choices=STAGES_CHOICE)
    startups_mentored = models.IntegerField(blank=True, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'MentorDetails'


# -------------------- PROJECTS --------------------
class Projects(models.Model):

    THEMES_CHOICE = InvestorDetails.THEMES_CHOICE

    CATEGORY_CHOICE = (
        ('HARDWARE', 'HARDWARE'),
        ('SOFTWARE', 'SOFTWARE')
    )

    SECTOR_CHOICE = (
        ('Central Ministry', 'Central Ministry'),
        ('State Government', 'State Government'),
        ('Private', 'Private'),
        ('Corporate', 'Corporate'),
        ('NGO', 'NGO'),
        ('Semi-Government', 'Semi-Government'),
        ('PSU', 'PSU')
    )

    organization_name = models.CharField(max_length=200)
    sector = models.CharField(max_length=100, choices=SECTOR_CHOICE)
    business_phone_number = models.CharField(max_length=15)
    document1 = models.FileField(upload_to='files/%Y/%m/%d/')
    document2 = models.FileField(upload_to='files/%Y/%m/%d/', blank=True)
    theme = models.CharField(max_length=100, choices=THEMES_CHOICE)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICE)
    problem_statement_title = models.TextField()
    problem_statement_description = models.TextField()
    demo_link = models.URLField(null=True, blank=True)
    dataset = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.problem_statement_title
