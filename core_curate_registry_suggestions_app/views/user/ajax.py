"""AJAX views for the Curate app
"""
import json
import logging
import re

import core_curate_app.views.user.forms as users_forms
from core_curate_app.components.curate_data_structure import api as curate_data_structure_api
from django.http import HttpResponse as HttpResponseAjax
from django.http.response import HttpResponse
from django.template import loader

import core_curate_registry_suggestions_app.views.user.forms as suggestions_forms
from core_curate_registry_app.views.user.ajax import StartCurate
from core_curate_registry_suggestions_app.components.suggestions import \
    api as curate_data_structure_registry_suggestions_api
from core_curate_registry_suggestions_app.components.suggestions.models import Suggestions
from core_curate_registry_suggestions_app.constants import DISAMBIGUATE_NAME_FORM
from core_curate_registry_suggestions_app.utils import sparql as sparql_api

logger = logging.getLogger(__name__)


def disambiguate_name(request):
    """ Disambiguate name.

    Args:
        request:

    Returns:

    """
    selected_option = request.POST['curate_form']

    if selected_option == "new" and request.POST['role'] == "organization":  # TODO check list of role enabled
        new_form = users_forms.NewForm(request.POST)
        name = new_form.data['document_name']

        # TODO: create a method to get list of names
        list_suggestions = sparql_api.get_entity_names(name)
        if len(list_suggestions) >= 1:
            form = suggestions_forms.DisambiguationForm(list_suggestions)
            context = {
                "disambiguate_form": form
            }

            return HttpResponse(
                json.dumps({
                    'form': loader.render_to_string(DISAMBIGUATE_NAME_FORM,
                                                    context)}),
                'application/javascript')

    return HttpResponseAjax(json.dumps({}), content_type='application/javascript')


def get_suggestions(request):
    """ Get suggestions.

    Args:
        request:

    Returns:

    """
    # TODO
    try:
        curate_data_structure = curate_data_structure_api.get_by_id(request.POST['id'])
        suggestion = curate_data_structure_registry_suggestions_api.get_by_curate_data_structure(curate_data_structure)
        sparqlUrl = suggestion.url
        # TODO delete suggestion
        # suggestion.delete()
        if sparqlUrl is not None:
            abstract = sparql_api.get_abstract(sparqlUrl)
            homepage = sparql_api.get_homepage(sparqlUrl)
            label = sparql_api.get_label(sparqlUrl)
            return HttpResponseAjax(json.dumps({'abstract': abstract, 'homepage': homepage, 'label': label}), content_type='application/javascript')
    except Exception as e:
        logger.warning("Something went wrong when retrieving suggestions.")

    return HttpResponseAjax(json.dumps({}), content_type='application/javascript')


class StartCurateSuggestions(StartCurate):
    """ Start Curate Suggestions
    """

    def post(self, request):
        """ Load forms to start curating.
            Add role to response url.

            Args:
               request:

            Returns:

        """
        response = super(StartCurateSuggestions, self).post(request)
        try:
            # Create suggestions in DB
            list_ids = re.findall("enter-data/(.*)\\?role", response.content.decode("utf-8"))
            if len(list_ids) == 1:
                curate_data_structure = curate_data_structure_api.get_by_id(list_ids[0])
                curate_data_structure_registry_suggestions_api.upsert(
                    Suggestions(url=request.POST.get('sparqlUrl', None), curate_data_structure=curate_data_structure))
        except Exception as e:
            logger.warning("Something went wrong with the suggestions.")
        return response
