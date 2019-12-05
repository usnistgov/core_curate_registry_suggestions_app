Core Curate Registry Suggestions App
====================================

Curation suggestions functionalities specific to the Registry application for the curator core project.

Quick start
===========

1. Add "core_curate_registry_suggestions_app" to your INSTALLED_APPS setting
----------------------------------------------------------------------------

.. code:: python

    INSTALLED_APPS = [
      ...
      'core_curate_registry_suggestions_app',
      'core_curate_registry_app',
      'core_curate_app',
    ]

2. Include the core_curate_registry_suggestions_app URLconf in your project urls.py
-----------------------------------------------------------------------------------

.. code:: python

    url(r'^curate/', include('core_curate_registry_suggestions_app.urls')),
