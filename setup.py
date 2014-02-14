from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(
	name='ckanext-villedemontreal',
	version=version,
	description="Arrondissement list",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Julio Alcantara',
	author_email='',
	url='',
	license='GNU',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.villedemontreal'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	ville_de_montreal=ckanext.villedemontreal.plugin:IDatasetVilledeMontrealPlugin
	facet_territoire=ckanext.villedemontreal.plugin:IFacetTerritoirePlugin
	""",
)
