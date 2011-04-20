# vim= ai ts=4 sts=4 et sw=4 encoding=utf-8
import unittest
from mangrove.datastore.question import IntegerQuestion, TextQuestion, SelectQuestion

class TestQuestion(unittest.TestCase):
    def setup(self):
        pass

    def test_should_create_text_question_type_for_default_english_language(self):
        expected_json = {
            "defaultValue": "some default value",
            "label": {"eng": "What is your name"},
            "name": "question1_Name",
            "question_code": "Q1",
            "type": "text"
        }
        question = TextQuestion(name="question1_Name", question_code="Q1", label="What is your name",
                                defaultValue="some default value", language="eng")

        actual_json = question._to_json()
        self.assertEqual(actual_json, expected_json)

    def test_should_create_integer_question_type_for_default_english_language(self):
        expected_json = {
            "label": {"eng": "What is your age"},
            "name": "Age",
            "question_code": "Q2",
            "range": {},
            "type": "integer",
            }
        question = IntegerQuestion(name="Age",  question_code="Q2", label="What is your age",
                                   language="eng")
        actual_json = question._to_json()
        self.assertEqual(actual_json, expected_json)

    def test_should_create_integer_question_type_for_default_english_language_with_range(self):
        expected_json = {
            "label": {"eng": "What is your age"},
            "name": "Age",
            "question_code": "Q2",
            "range": {"min": 15,"max": 120},
            "type": "integer",
            }
        question = IntegerQuestion(name="Age", question_code="Q2", label="What is your age",
                                   language="eng",range={"min": 15,"max": 120})
        actual_json = question._to_json()
        self.assertEqual(actual_json, expected_json)

    def test_should_create_select_one_question_type_for_default_english_language(self):
        expected_json = {
            "label": {"eng": "What is your favorite color"},
            "name": "color",
            "options": [{"text": [{"eng": "RED"}],"val": 1},{"text": [{"eng": "YELLOW"}],"val": 2},{"text":[{"eng":"green"}]}],
            "question_code": "Q3",
            "type": "select1",
            }
        question = SelectQuestion(name="color", question_code="Q3", label="What is your favorite color",
                                   language="eng",options=[("RED",1),("YELLOW",2),('green')])
        actual_json = question._to_json()
        self.assertEqual(actual_json, expected_json)


    def test_should_add_label_for_french_language(self):
        expected_json = {
            "defaultValue": "some default value",
            "label": {"eng": "What is your name","fra":"french label"},
            "name": "question1_Name",
            "question_code": "Q1",
            "type": "text"
        }
        question = TextQuestion(name="question1_Name", question_code="Q1", label="What is your name",
                                defaultValue="some default value" )
        question.add_or_edit_label(language="fra",label="french label")
        actual_json = question._to_json()
        self.assertEqual(actual_json, expected_json)

    def test_should_edit_label_for_english_language(self):
        expected_json = {
            "defaultValue": "some default value",
            "label": {"eng": "english label","fra":"french label"},
            "name": "question1_Name",
            "question_code": "Q1",
            "type": "text"
        }
        question = TextQuestion(name="question1_Name", question_code="Q1", label="What is your name",
                                defaultValue="some default value" )
        question.add_or_edit_label(language="fra",label="french label")
        question.add_or_edit_label(label="english label")
        actual_json = question._to_json()
        self.assertEqual(actual_json, expected_json)
