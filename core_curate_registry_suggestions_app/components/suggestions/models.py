""" Suggestions model
"""
from core_curate_app.components.curate_data_structure.models import CurateDataStructure
from core_main_app.commons import exceptions
from django_mongoengine import fields, Document
from mongoengine import errors as mongoengine_errors
from mongoengine.errors import NotUniqueError
from mongoengine.queryset.base import CASCADE


class Suggestions(Document):
    """ Suggestions.
    """

    url = fields.StringField()
    curate_data_structure = fields.ReferenceField(CurateDataStructure, reverse_delete_rule=CASCADE) #TODO unique

    def save_object(self):
        """ Custom save

        Returns:

        """
        try:
            return self.save()
        except NotUniqueError:
            raise exceptions.ModelError("Unable to save the document: not unique.")
        except Exception as ex:
            raise exceptions.ModelError(str(ex))

    @staticmethod
    def get_by_id(suggestions_id):
        """ Return the object with the given id.

        Args:
            suggestions_id:

        Returns:
            Suggestions (obj): Suggestions object with the given id

        """
        try:
            return Suggestions.objects.get(pk=str(suggestions_id))
        except mongoengine_errors.DoesNotExist as e:
            raise exceptions.DoesNotExist(str(e))
        except Exception as ex:
            raise exceptions.ModelError(str(ex))

    @staticmethod
    def get_by_curate_data_structure(curate_data_structure):
        """ Returns the suggestions with the given curate_data_structure

        Args:
            curate_data_structure:

        Returns:

        """
        return Suggestions.objects.get(curate_data_structure=curate_data_structure)
