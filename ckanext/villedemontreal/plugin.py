import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as tk

# FIXME OrderedDict should be available via the toolkit
try:
    #from collections import OrderedDict # 2.7
    from ckan.common import OrderedDict
    from ckan.lib.base import g
except ImportError:
    from sqlalchemy.util import OrderedDict

def create_territoires():
    '''Create territoires vocab and tags, if they don't exist already.

    Note that you could also create the vocab and tags using CKAN's API,
    and once they are created you can edit them (e.g. to add and remove
    possible dataset territoire code values) using the API.

    '''
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        data = {'id': 'territoires'}
        tk.get_action('vocabulary_show')(context, data)
        logging.info("Territoires genre vocabulary already exists, skipping.")
    except tk.ObjectNotFound:
        logging.info("Creating vocab 'territoires'")
        data = {'name': 'territoires'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        
        for tag in (u"AHUNTSIC-CARTIE".lower(), u"AGGLOMERATION".lower(), u"ANJOU".lower(), u"CDN-NDG".lower(), u"LACHINE".lower(), 
                    u"LASALLE".lower(), u"PLAT-MT-ROYAL".lower(), u"SUD-OUEST".lower(), u"BI-STE-GE".lower(), 
                    u"MERC-HOCH-MA".lower(), u"MONTREAL".lower(), u"MONTREAL-NORD".lower(), u"OUTREMONT".lower(), 
                    u"PIERREF-ROXBORO".lower(), u"RDP-PAT".lower(), u"RSMT-PETITE-PAT".lower(), 
                    u"ST-LAURENT".lower(), u"ST-LEONARD".lower(), u"VERDUN".lower(), 
                    u"VILLE-MARIE".lower(), u"VILL-ST-M-P-EXT".lower()):
            logging.info(
                    "Adding tag {0} to vocab 'territoires'".format(tag))
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            print data
            tk.get_action('tag_create')(context, data)


def territoires():
    '''Return the list of territoire codes from the territoire codes vocabulary.'''
    create_territoires()
    try:
        territoires = tk.get_action('tag_list')(
                data_dict={'vocabulary_id': 'territoires'})
        return territoires
    except tk.ObjectNotFound:
        return None

def create_frequences_de_mise_a_jour():
    '''Create frequences_de_mise_a_jour vocab and tags, if they don't exist already.

    Note that you could also create the vocab and tags using CKAN's API,
    and once they are created you can edit them (e.g. to add and remove
    possible dataset frequences_de_mise_a_jour code values) using the API.

    '''
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        data = {'id': 'frequences_de_mise_a_jour'}
        tk.get_action('vocabulary_show')(context, data)
        logging.info("frequences_de_mise_a_jour genre vocabulary already exists, skipping.")
    except tk.ObjectNotFound:
        logging.info("Creating vocab 'frequences_de_mise_a_jour'")
        data = {'name': 'frequences_de_mise_a_jour'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        
        for tag in (u"En temps reel", u"Quotidienne", u"Hebdomadaire", 
                    u"Mensuelle", u"Annuelle", u"Ponctuelle", u"Ponctuelle", 
                    u"Tous les cinq ans", u"Aucune", u"Variable"):
            logging.info(
                    "Adding tag {0} to vocab 'frequences_de_mise_a_jour'".format(tag))
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            print data
            tk.get_action('tag_create')(context, data)


def frequences_de_mise_a_jour():
    '''Return the list of frequences_de_mise_a_jour codes from the frequences_de_mise_a_jour codes vocabulary.'''
    create_frequences_de_mise_a_jour()
    try:
        frequences_de_mise_a_jour = tk.get_action('tag_list')(
                data_dict={'vocabulary_id': 'frequences_de_mise_a_jour'})
        return frequences_de_mise_a_jour
    except tk.ObjectNotFound:
        return None
        
        
def create_unites_geographique():
    '''Create unites_geographique vocab and tags, if they don't exist already.

    Note that you could also create the vocab and tags using CKAN's API,
    and once they are created you can edit them (e.g. to add and remove
    possible dataset unites_geographique code values) using the API.

    '''
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        data = {'id': 'unites_geographique'}
        tk.get_action('vocabulary_show')(context, data)
        logging.info("unites_geographique genre vocabulary already exists, skipping.")
    except tk.ObjectNotFound:
        logging.info("Creating vocab 'unites_geographique'")
        data = {'name': 'unites_geographique'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        
        for tag in (u"Aire de recensement", u"Code postal", u"Cadastre", 
                    u"District electoral Section de vote", u"Coordonnees georeferencees", 
                    u"Limites des anciens territoires administratifs", u"Geolocalisation", 
                    u"Lieux de services", u"Longitude  Latitude"):
            logging.info(
                    "Adding tag {0} to vocab 'unites_geographique'".format(tag))
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            print data
            tk.get_action('tag_create')(context, data)


def unites_geographique():
    '''Return the list of unite geographique from the unites_geographique codes vocabulary.'''
    create_unites_geographique()
    try:
        unites_geographique = tk.get_action('tag_list')(
                data_dict={'vocabulary_id': 'unites_geographique'})
        return unites_geographique
    except tk.ObjectNotFound:
        return None
        
class IFacetTerritoirePlugin(plugins.SingletonPlugin):
	
    plugins.implements(plugins.IFacets, inherit=True)

    def dataset_facets(self, facets_dict, package_type):

        #facets = OrderedDict()
        #print (package_type)
        if package_type <> 'dataset':
			return facets_dict
        
        default_facet_titles = {
                    'res_format': tk._('Formats'),
                    'groups': tk._('Groups'),
                    'organization': tk._('Organizations'),
                    'tags': tk._('Tags'),
                    'vocab_territoires': tk._('Territoires'),
                    'license_id': tk._('License'),                    
                    }
        #for facet in g.facets:
		#	if facet in default_facet_titles:
		#		facets[facet] = default_facet_titles[facet]
		#	else:
		#		facets[facet] = facet
		#
        #facets_dict = default_facet_titles
        

        return default_facet_titles

class IDatasetVilledeMontrealPlugin(plugins.SingletonPlugin,
        tk.DefaultDatasetForm):
    '''An IDatasetForm CKAN plugin (IDatasetVilledeMontrealPlugin).

    Uses a tag vocabulary to add a territoire custom metadata field to datasets.

    '''
    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.IDatasetForm, inherit=False)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)

    # These record how many times methods that this plugin's methods are
    # called, for testing purposes.
    num_times_new_template_called = 0
    num_times_read_template_called = 0
    num_times_edit_template_called = 0
    num_times_comments_template_called = 0
    num_times_search_template_called = 0
    num_times_history_template_called = 0
    num_times_package_form_called = 0
    num_times_check_data_dict_called = 0
    num_times_setup_template_variables_called = 0

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')

    def get_helpers(self):
        return {'territoires': territoires,
                'frequences_de_mise_a_jour':frequences_de_mise_a_jour,
                'unites_geographique':unites_geographique}

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def _modify_package_schema(self, schema):
        # Add our custom territoire metadata field to the schema.
        schema.update({
                'territoire': [tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_tags')('territoires')]
                })
        # Add our custom_test metadata field to the schema, this one will use
        # convert_to_extras instead of convert_to_tags.
        
        # Add custom periode_couverte as extra field
        schema.update({
                'periode_couverte': [tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')]
                })
                
        # Add custom frequences_de_mise_a_jour as extra field
        schema.update({
                'frequence_de_mise_a_jour': [tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_tags')('frequences_de_mise_a_jour')]
                })
                
        # Add custom unite_administrative as extra field
        schema.update({
                'unite_administrative': [tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')]
                })

        # Add custom methodologie as extra field
        schema.update({
                'methodologie': [tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')]
                })
                
        # Add custom premiere_date_de_publication as extra field
        schema.update({
                'premiere_date_de_publication': [tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')]
                })
                
        # Add custom unite_geographique as extra field
        schema.update({
                'unite_geographique': [tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_tags')('unites_geographique')]
                })
                
        return schema

    def create_package_schema(self):
        schema = super(IDatasetVilledeMontrealPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(IDatasetVilledeMontrealPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(IDatasetVilledeMontrealPlugin, self).show_package_schema()

        # Don't show vocab tags mixed in with normal 'free' tags
        # (e.g. on dataset pages, or on the search page)
        schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))

        # Add our custom territoire metadata field to the schema.
        schema.update({
            'territoire': [
                tk.get_converter('convert_from_tags')('territoires'),
                tk.get_validator('ignore_missing')]
            })

        # Add our periode_couverte field to the dataset schema.
        schema.update({
            'periode_couverte': [tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing')]
            })
            
        # Add our frequences_de_mise_a_jour field to the dataset schema.
        schema.update({
            'frequence_de_mise_a_jour': [tk.get_converter('convert_from_tags')('frequences_de_mise_a_jour'),
                tk.get_validator('ignore_missing')]
            })
            
        # Add our unite_administrative field to the dataset schema.
        schema.update({
            'unite_administrative': [tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing')]
            })

        # Add our methodologie field to the dataset schema.
        schema.update({
            'methodologie': [tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing')]
            })
            
        # Add our premiere_date_de_publication field to the dataset schema.
        schema.update({
            'premiere_date_de_publication': [tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing')]
            })
            
        # Add our unite_geographique field to the dataset schema.
        schema.update({
            'unite_geographique': [tk.get_converter('convert_from_tags')('unites_geographique'),
                tk.get_validator('ignore_missing')]
            })
            

        return schema

    # These methods just record how many times they're called, for testing
    # purposes.
    # TODO: It might be better to test that custom templates returned by
    # these methods are actually used, not just that the methods get
    # called.

    def setup_template_variables(self, context, data_dict):
        IDatasetVilledeMontrealPlugin.num_times_setup_template_variables_called += 1
        return super(IDatasetVilledeMontrealPlugin, self).setup_template_variables(
                context, data_dict)

    def new_template(self):
        IDatasetVilledeMontrealPlugin.num_times_new_template_called += 1
        return super(IDatasetVilledeMontrealPlugin, self).new_template()

    def read_template(self):
        IDatasetVilledeMontrealPlugin.num_times_read_template_called += 1
        return super(IDatasetVilledeMontrealPlugin, self).read_template()

    def edit_template(self):
        IDatasetVilledeMontrealPlugin.num_times_edit_template_called += 1
        return super(IDatasetVilledeMontrealPlugin, self).edit_template()

    def comments_template(self):
        IDatasetVilledeMontrealPlugin.num_times_comments_template_called += 1
        return super(IDatasetVilledeMontrealPlugin, self).comments_template()
    
    def search_template(self):
        IDatasetVilledeMontrealPlugin.num_times_search_template_called += 1
        return super(IDatasetVilledeMontrealPlugin, self).search_template()

    def history_template(self):
        IDatasetVilledeMontrealPlugin.num_times_history_template_called += 1
        return super(IDatasetVilledeMontrealPlugin, self).history_template()

    def package_form(self):
        IDatasetVilledeMontrealPlugin.num_times_package_form_called += 1
        return super(IDatasetVilledeMontrealPlugin, self).package_form()

    # check_data_dict() is deprecated, this method is only here to test that
    # legacy support for the deprecated method works.
    def check_data_dict(self, data_dict, schema=None):
        IDatasetVilledeMontrealPlugin.num_times_check_data_dict_called += 1
