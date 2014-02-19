CKAN Ville de Montréal Extension
================================

This extension is developed basing on the extension (example_idatasetform), with the variant type to add custom fields and tags extra. 

With this variant the extension lets you create a territoire facet that identifies an area within a city (Montréal is composed of territories). 

Similarly, several fields (closed and open) are created.

Requirements
------------

Before installing ckanext-villedemontreal, make sure that you have installed the following:

* CKAN 2.1+

Installation
------------

Install the plugin using pip. Download it, then from the ckanext- villedemontreal directory, run


::

    $ pip install -e git+https://github.com/VilledeMontreal/CKAN-Extension-Territoire.git#egg=ckanext-territoire



This will register a plugin entry point, so you can now add the following 
to the ``[app:main]`` section of your CKAN .ini file:

::

    ckan.plugins = ville_de_montreal, facet_territoire <other-plugins>

After you reload the site, the Ville de Montreal plugin, custom fields and facet champs should be available when you create a new dataset.

