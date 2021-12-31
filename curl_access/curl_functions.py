import json
import logging

logger = logging.getLogger(__name__)

json_file = open('resources/data.json')
data = json.load(json_file)


def get_houms():
    """Return all houms that are registered in the system

    :return: a list of houm object.
    :rtype: list of dict
    """
    return data.get("houmers", [])


def get_visitors():
    """Return all visitors that are registered in the system

    :return: a list of visitor object.
    :rtype: list of dict
    """
    return data.get("visitors", [])


def get_places():
    """Return all places that are registered in the system

    :return: a list of place object.
    :rtype: list of dict
    """
    return data.get("places", [])


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


def __filter_by_identifier(items, identifier):
    """Filter items by identifier

    :param list items: list of items to take into account during the filter

    :return: first element from the filtered data
    :rtype: dict

    :raise: IndexError: that means there is not any element with this identifier in the items list
    """
    res = [item for item in items if item['id'] == identifier]
    return res[0]
