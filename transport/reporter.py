# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
from mangrove.datastore.data import EntityAggregration
from mangrove.datastore.entity import Entity

from mangrove.errors.MangroveException import NumberNotRegisteredException, MultipleReportersForANumberException
from mangrove.datastore import data
from mangrove.form_model.form_model import MOBILE_NUMBER_FIELD, NAME_FIELD

REPORTER_ENTITY_TYPE = ["reporter"]


def find_reporter(dbm, from_number):
    from_reporter_list = find_reporters_by_from_number(dbm, from_number)
    return [each.values()[0] for each in from_reporter_list]


def find_reporter_entity(dbm, from_number):
    reporter_list = find_reporters_by_from_number(dbm, from_number)
    if len(reporter_list) > 1:
        raise MultipleReportersForANumberException(from_number)
    reporter_entity_id = reporter_list[0].keys()[0]
    return Entity.get(dbm, reporter_entity_id)


def find_reporters_by_from_number(dbm, from_number):
    reporters = data.aggregate(dbm, entity_type=REPORTER_ENTITY_TYPE,
                               aggregates={MOBILE_NUMBER_FIELD: data.reduce_functions.LATEST,
                                           NAME_FIELD: data.reduce_functions.LATEST}, aggregate_on=EntityAggregration()
    )
    from_reporter_list = [{id: reporters[id]} for id in reporters if
                                              reporters[id].get(MOBILE_NUMBER_FIELD) == from_number]
    if not len(from_reporter_list):
        raise NumberNotRegisteredException(from_number)
    return from_reporter_list