
from mangrove.contrib.registration_validators import MobileNumberValidationsForReporterRegistrationValidator, AtLeastOneLocationFieldMustBeAnsweredValidator
from mangrove.form_model.validators import MandatoryValidator
from mangrove.form_model.field import HierarchyField, TextField, TelephoneNumberField, GeoCodeField, ShortCodeField
from mangrove.form_model.form_model import ENTITY_TYPE_FIELD_NAME, ENTITY_TYPE_FIELD_CODE, NAME_FIELD, NAME_FIELD_CODE, SHORT_CODE, SHORT_CODE_FIELD, LOCATION_TYPE_FIELD_NAME, LOCATION_TYPE_FIELD_CODE, MOBILE_NUMBER_FIELD, MOBILE_NUMBER_FIELD_CODE, GEO_CODE_FIELD_NAME, FormModel, GEO_CODE, REGISTRATION_FORM_CODE, EMAIL_FIELD, EntityFormModel, \
    TAG, TAG_FIELD_CODE
from mangrove.form_model.validation import TextLengthConstraint, RegexConstraint, ShortCodeRegexConstraint

GLOBAL_REGISTRATION_FORM_CODE = "reg"

def create_default_reg_form_model(manager):
    form_model = construct_global_registration_form(manager)
    form_model.save()
    return form_model


def _create_constraints_for_mobile_number():
    #constraints on questionnaire
    mobile_number_length = TextLengthConstraint(max=15, min=5)
    mobile_number_pattern = RegexConstraint(reg='^[0-9]+$')
    mobile_constraints = [mobile_number_length, mobile_number_pattern]
    return mobile_constraints


def construct_global_registration_form(manager):
    question1 = HierarchyField(name=ENTITY_TYPE_FIELD_NAME, code=ENTITY_TYPE_FIELD_CODE,
                               label="What is associated subject type?" , instruction="Enter a type for the subject")

    question2 = TextField(name=NAME_FIELD, code=NAME_FIELD_CODE, label="What is the subject's name?",
                          defaultValue="some default value" ,
                          instruction="Enter a subject name", constraints=[TextLengthConstraint(max=80)], required=True)
    question3 = ShortCodeField(name=SHORT_CODE_FIELD, code=SHORT_CODE, label="What is the subject's Unique ID Number",
                          defaultValue="some default value" ,
                          instruction="Enter a id, or allow us to generate it",
                           constraints=[TextLengthConstraint(max=12), ShortCodeRegexConstraint(reg='^[a-zA-Z0-9]+$')], required=False)
    question4 = TextField(name=TAG, code=TAG_FIELD_CODE, label="What is the Tag?",
                          defaultValue="some default value" ,
                          instruction="Enter Tag", constraints=[TextLengthConstraint(max=225)], required=False)

    question5 = GeoCodeField(name=GEO_CODE_FIELD_NAME, code=GEO_CODE, label="What is the subject's GPS co-ordinates?" , instruction="Enter lat and long. Eg 20.6, 47.3", required=False)
    question6 = TelephoneNumberField(name=MOBILE_NUMBER_FIELD, code=MOBILE_NUMBER_FIELD_CODE,
                                     label="What is the mobile number associated with the subject?",
                                     defaultValue="some default value" ,
                                     instruction="Enter the subject's number", constraints=(
            _create_constraints_for_mobile_number()), required=True)
    question7 = TextField(name=EMAIL_FIELD, code=EMAIL_FIELD, label="What is the subject's email",
                          defaultValue="" ,
                          instruction="Enter email id", constraints=[TextLengthConstraint(max=50)], required=False)
    question8 = HierarchyField(name=LOCATION_TYPE_FIELD_NAME, code=LOCATION_TYPE_FIELD_CODE,
                               label="What is the subject's location?" , instruction="Enter a region, district, or commune", required=False)
    form_model = EntityFormModel(manager, name=GLOBAL_REGISTRATION_FORM_CODE, form_code=REGISTRATION_FORM_CODE, fields=[
        question1, question2, question3, question4, question5, question6, question7, question8], is_registration_model=True, entity_type=["registration"],
        validators=[MandatoryValidator(), MobileNumberValidationsForReporterRegistrationValidator(),
                    AtLeastOneLocationFieldMustBeAnsweredValidator()])
    return form_model