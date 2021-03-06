import os
from setuptools import setup, find_packages


version = '1.17.6.dev0'


tests_require = [
    'Products.CMFCore',
    'Zope2',
    'ftw.builder',
    'ftw.testbrowser',
    'ftw.testing',
    'plone.app.contenttypes',
    'plone.app.testing',
    'plone.browserlayer',
    'plone.mocktestcase',
    'plone.api',
    'plone.restapi',
    'plone.testing',
    'transaction',
    'zope.configuration',
    'zope.dottedname',
    ]


extras_require = {
    'tests': tests_require,
    'deletepermission': [
        'collective.deletepermission',
    ]}


setup(name='ftw.lawgiver',
      version=version,
      description='Generate your Plone workflows by describing it in' + \
          ' plain text with a DSL.',

      long_description=open('README.rst').read() + '\n' + \
          open(os.path.join('docs', 'HISTORY.txt')).read(),

      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone :: 5.1',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],

      keywords='ftw lawgiver generate workflows dsl',
      author='4teamwork AG',
      author_email='mailto:info@4teamwork.ch',
      url='https://github.com/4teamwork/ftw.lawgiver',

      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw', ],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'AccessControl',
        'Acquisition',
        'Plone',
        'Products.CMFCore',
        'Products.CMFPlone',
        'Products.GenericSetup',
        'Products.statusmessages',
        'ZODB3',
        'Zope2',
        'argparse',
        'ftw.upgrade',
        'i18ndude',
        'lxml',
        'ordereddict',
        'path.py',
        'plone.app.workflow',
        'plone.i18n',
        'setuptools',
        'zope.component',
        'zope.configuration',
        'zope.i18n',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.publisher',
        'zope.schema',
        ],

      tests_require=tests_require,
      extras_require=extras_require,

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone

      [zopectl.command]
      rebuild_workflows = ftw.lawgiver.commands:rebuild_workflows
      """,
      )
