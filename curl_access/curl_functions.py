import json
import logging
from _datetime import datetime

logger = logging.getLogger(__name__)

json_file = open('resources/data.json')
data = json.load(json_file)


def get_houm(identifier):
    """Return a houm by his identifier

    :param int identifier: houmer identifier

    :return: a full houm object
    :rtype: dict or None if this does not exist
    """
    try:
        return __filter_by_identifier(get_houms(), identifier)
    except IndexError:
        logger.debug("Houm with Id: %s doesn't exist on the system" % (identifier,))
        return None


def get_houms():
    """Return all houms that are registered in the system

    :return: a list of houm object.
    :rtype: list of dict
    """
    return data.get("houmers", [])


def get_visited_places_by_houmer(houmer_id, date):
    """Get visited places bu houmer

    Get visited places by a houmer in a specific date, it's going
    to calculate also the time that was spent in the visit

    :param int houmer_id: Houmer identifier
    :param str date: date in format 'Y-m-d H:M:S' to take into account
                    at the filter time

    :return: a Houm object that matches with identifier and date
    :rtype: dict
    """
    visited_items = list(filter(
        lambda visited:
        (visited['houmer'] == houmer_id) and (__is_in_day(visited["started_at"], visited["completed_at"], date)),
        data.get("visited", [])
    ))

    def update_custom_information(item, time): return item.update(
        {
            "spent_time": str(time),
            "place": get_place(item["place"])
        }
    ) or item

    res = [update_custom_information(item, __get_time(item)) for item in visited_items]
    return res


def __get_time(item):
    """Get time between start and end times in the item

    Calculate the time that are between start time and end time,
    this is going to represent the spent time in the visit to an specific place

    :param dict item: item with attributes start and end time

    :return: returns time delta that results by the operation end - start date
    :rtype: datetime.timedelta
    """
    start_time = datetime.strptime(item['started_at'], '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(item['completed_at'], '%Y-%m-%d %H:%M:%S')
    return end_time - start_time


def __is_in_day(start_date, end_date, date):
    """Verifies if a date is in a specified range of dates

    :param dict start_date: start date for the range
    :param dict end_date: end date for the range
    :param dict date: date to be verified into the range

    :return: returns true if it's in the rage, else false
    :rtype: bool
    """
    start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    end_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')
    date = datetime.strptime(date, '%Y-%m-%d')
    return (start_date.day == date.day
            and start_date.month == date.month
            and start_date.year == date.year) or \
           (end_date.day == date.day
            and end_date.month == date.month
            and end_date.year == date.year)


def get_visitor(identifier):
    """Return a visitor by its identifier

    :param int identifier: visitor identifier

    :return: a full visitor object
    :rtype: dict or None if this does not exist
    """
    try:
        return __filter_by_identifier(get_visitors(), identifier)
    except IndexError:
        logger.debug("Visitor with Id: %s doesn't exist on the system" % (identifier,))
        return None


def get_visitors():
    """Return all visitors that are registered in the system

    :return: a list of visitor object.
    :rtype: list of dict
    """
    return data.get("visitors", [])


def get_place(identifier):
    """Return a place by its identifier

    :param int identifier: place identifier

    :return: a full place object
    :rtype: dict or None if this does not exist
    """
    try:
        return __filter_by_identifier(get_places(), identifier)
    except IndexError:
        logger.debug("Place with Id: %s doesn't exist on the system" % (identifier,))
        return None


def get_places():
    """Return all places that are registered in the system

    :return: a list of place object.
    :rtype: list of dict
    """
    return data.get("places", [])


def __filter_by_identifier(items, identifier):
    """Filter items by identifier

    :param list items: list of items to take into account during the filter

    :return: first element from the filtered data
    :rtype: dict

    :raise: IndexError: that means there is not any element with this identifier in the items list
    """
    res = [item for item in items if item['id'] == identifier]
    return res[0]
