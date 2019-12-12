""" Suggestions API
"""

from core_curate_registry_suggestions_app.components.suggestions.models import Suggestions


def get_by_id(suggestions_id):
    """ Returns the suggestions with the given id

    Args:
        suggestions_id:

    Returns:

    """
    return Suggestions.get_by_id(suggestions_id)


def get_by_curate_data_structure(curate_data_structure):
    """ Returns the suggestions with the given curate_data_structure

    Args:
        curate_data_structure:

    Returns:

    """
    return Suggestions.get_by_curate_data_structure(curate_data_structure)


def upsert(suggestions):
    """ Save or update the Suggestions

    Args:
        suggestions:

    Returns:

    """
    return suggestions.save_object()
