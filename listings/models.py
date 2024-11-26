from django.db import models

class RequiredSkill(models.Model):
    name = models.TextField(null=False)

    class Meta:
        db_table = 'required_skill'

class Professor(models.Model):
    first_name = models.TextField(null=False)
    last_name = models.TextField(null=False)
    email = models.TextField(null=False)
    hire_date = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    password = models.TextField(null=False)
    birth_date = models.TextField(null=True)
    phone_number = models.TextField(null=True)
    salary = models.TextField(null=True)
    professor_number = models.TextField(null=True)

    class Meta:
        db_table = 'professor'

class GainedSkill(models.Model):
    name = models.TextField(null=False)

    class Meta:
        db_table = 'gained_skill'

class Department(models.Model):
    name = models.TextField(null=False)
    description = models.TextField(null=True)
    department_code = models.TextField(null=True)
    created_date = models.TextField(null=True)
    phone_number = models.TextField(null=True)
    email = models.TextField(null=True)

    class Meta:
        db_table = 'department'

class Course(models.Model):
    title = models.TextField(null=False)
    department = models.ForeignKey(
        'Department', on_delete=models.SET_NULL, null=True, related_name='courses'
    )
    is_completed = models.BooleanField(default=False)
    course_manager_email = models.TextField(null=True)
    client_company_name = models.TextField(null=True)
    contract_number = models.TextField(null=True)
    invoice_status = models.TextField(null=True)
    contract_start_date = models.TextField(null=True)
    approval_status = models.TextField(null=True)

    class Meta:
        db_table = 'course'


