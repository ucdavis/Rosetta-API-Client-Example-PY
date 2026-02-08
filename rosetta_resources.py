#!/usr/bin/env python3

'''
    Title: rosetta_resources.py
    Authors: Dean Bunn and Wilson Miller
    Last Edit: 2026-02-07
'''

#Class for Rosetta API Information
class Rosetta_API_Info:
    def __init__(self):
        self.base_url = ""
        self.token_url = ""
        self.client_id = ""
        self.client_secret = ""
        self.oath_token = ""
        self.test_id = ""


#Class for Rosetta Person Information
class Rosetta_Person_Info:
    def __init__(self):
        self.iam_id = ""
        self.displayname = ""
        self.birth_date = ""
        self.manager_iam_id = ""
        self.provisioning_status_primary = ""
        self.name_lived_first_name = ""
        self.name_lived_middle_name = ""
        self.name_lived_last_name = ""
        self.name_legal_first_name = ""
        self.name_legal_middle_name = ""
        self.name_legal_last_name = ""
        self.id_iam_id = ""
        self.id_login_id = ""
        self.id_student_id = ""
        self.id_mothra_id = ""
        self.id_employee_id = ""
        self.id_mail_id = ""
        self.id_pidm = ""
        self.email_primary = ""
        self.email_work = ""
        self.email_personal = ""
        self.phone_primary = ""
        self.phone_personal = ""
        self.modified_date = ""
        self.affiliation = []
        self.employment_status = []
        self.student_association = []
        self.payroll_association = []



#Class for Rosetta Student Association
class Rosetta_Student_Association:
    def __init__(self):
        self.academic_level = ""
        self.class_level = ""
        self.college = ""
        self.major = ""



#Class for Rosetta Payroll Association
class Rosetta_Payroll_Association:
    def __init__(self):
        self.employee_record = ""
        self.employee_id = ""
        self.position_number = ""
        self.position_title  = ""
        self.relationship_to_organization = ""         
        self.employee_classification = ""
        self.employee_classification_description = ""
        self.status = ""
        self.hire_date = ""
        self.start_date = ""
        self.termination_date = ""
        self.fte_percentage = ""
        self.reports_to_position = ""
        self.job_type_id = ""
        self.job_type_description = ""
        self.job_family_id = ""
        self.job_family_description = ""
        self.organization_id = ""
        self.organization_title = ""
        self.division_id = ""
        self.division_title = ""
        self.subdivision_id = ""
        self.subdivision_title = ""
        self.business_unit_id = ""
        self.business_unit_title = ""
        self.department_id = ""
        self.department_title = ""
        self.department_short_title = ""



