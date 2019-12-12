""" Curate Registry Suggestions views

"""

from core_curate_registry_app.views.user.views import StartCurate, EnterDataRegistryView
from core_curate_registry_suggestions_app.constants import DISAMBIGUATE_JS, DISAMBIGUATE_RAW_JS, \
    DISAMBIGUATE_NAME_MODAL, CREATE_SUGGESTIONS_JS, CREATE_SUGGESTIONS_RAW_JS


class StartCurateSuggestions(StartCurate):
    """ Start Curate Suggestions
    """
    def __init__(self):
        super(StartCurateSuggestions, self).__init__()

        self.assets['js'].extend((
            {
                "path": DISAMBIGUATE_JS,
                "is_raw": False
            },
            {
                "path": DISAMBIGUATE_RAW_JS,
                "is_raw": True
            },
        ))
        self.modals.extend([DISAMBIGUATE_NAME_MODAL])


class EnterDataRegistrySuggestionsView(EnterDataRegistryView):
    """ Enter Data Registry Suggestions
    """
    def __init__(self):
        super(EnterDataRegistrySuggestionsView, self).__init__()

        self.assets['js'].extend((
            {
                "path": CREATE_SUGGESTIONS_JS,
                "is_raw": False
            },
            {
                "path": CREATE_SUGGESTIONS_RAW_JS,
                "is_raw": True
            },
        ))

    def build_context(self, request, curate_data_structure, reload_unsaved_changes):
        context = super(EnterDataRegistrySuggestionsView, self).build_context(request, curate_data_structure, reload_unsaved_changes)
        context['curate_data_structure_id'] = str(curate_data_structure.id)
        return context
