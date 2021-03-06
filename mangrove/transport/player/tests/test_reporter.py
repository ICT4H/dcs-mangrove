from mangrove.datastore.entity import create_entity
from mangrove.datastore.entity_type import define_type
from mangrove.errors.MangroveException import  NumberNotRegisteredException
from mangrove.form_model.form_model import MOBILE_NUMBER_FIELD, NAME_FIELD
from mangrove.transport.repository.reporters import find_reporter
# from mangrove.transport.repository.reporters import find_reporter, get_reporters_who_submitted_data_for_frequency_period
from mangrove.utils.test_utils.mangrove_test_case import MangroveTestCase


class TestReporter(MangroveTestCase):
    @classmethod
    def register(cls, manager, entity_type, data, location, source, aggregation_paths=None, short_code=None):
    #    manager = get_db_manager()
        e = create_entity(manager, entity_type=entity_type, location=location, aggregation_paths=aggregation_paths,
            short_code=short_code)
        e.add_data(data=data)
        return e

    def setUp(self):
        MangroveTestCase.setUp(self)
        define_type(self.manager, ["reporter"])
        #Register Reporter
        self.first_reporter = self.register(self.manager, entity_type=["reporter"],
            data=[(MOBILE_NUMBER_FIELD, "1234567890"),
                  (NAME_FIELD, "A")],
            location=[],
            source="sms", short_code="REP1")
        self.register(self.manager, entity_type=["reporter"],
            data=[(MOBILE_NUMBER_FIELD, "8888567890"),
                  (NAME_FIELD, "B")],
            location=[],
            source="sms", short_code="rep5")
        self.register(self.manager, entity_type=["reporter"],
            data=[(MOBILE_NUMBER_FIELD, "1234567890"),
                  (NAME_FIELD, "B")],
            location=[],
            source="sms", short_code="REP2")

        self.register(self.manager, entity_type=["reporter"],
            data=[(MOBILE_NUMBER_FIELD, "1234567891"),
                  (NAME_FIELD, "C")],
            location=[],
            source="sms", short_code="REP3")

    def tearDown(self):
        MangroveTestCase.tearDown(self)

    def test_should_load_reporter_list_given_tel_number(self):
        saved_r2 = find_reporter(self.manager, "8888567890")
        self.assertIsNotNone(saved_r2)
        self.assertEqual(1, len(saved_r2))
        self.assertEquals(saved_r2[0]["name"], "B")
        self.assertEquals(saved_r2[0]["mobile_number"], "8888567890")

    def test_should_raise_exception_if_no_reporter_for_tel_number(self):
        with self.assertRaises(NumberNotRegisteredException):
            find_reporter(self.manager, "X")

    def test_should_not_raise_exception_if_multiple_reporters_for_a_number(self):
        reporter_list = find_reporter(self.manager, "1234567890")
        self.assertEqual(2, len(reporter_list))
        self.assertTrue({NAME_FIELD: "A", MOBILE_NUMBER_FIELD: "1234567890"} in reporter_list)
        self.assertTrue({NAME_FIELD: "B", MOBILE_NUMBER_FIELD: "1234567890"} in reporter_list)
