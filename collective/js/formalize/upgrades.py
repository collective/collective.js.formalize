from Products.CMFCore.utils import getToolByName

def upgrade_1000_1001(context):
    setup = getToolByName(context, 'portal_setup')
    jsregistry = getToolByName(context, 'portal_javascripts')
    jsregistry.unregisterResource('++resource++collective.js.formalize/js/formalize.js')
    setup.runImportStepFromProfile('profile-collective.js.formalize:default',
                                   'jsregistry', run_dependencies=False,
                                   purge_old=False)
    jsregistry.cookResources()
