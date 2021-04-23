# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import kuleuven.subsites


class KuleuvenSubsitesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=kuleuven.subsites)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'kuleuven.subsites:default')


KULEUVEN_SUBSITES_FIXTURE = KuleuvenSubsitesLayer()


KULEUVEN_SUBSITES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(KULEUVEN_SUBSITES_FIXTURE,),
    name='KuleuvenSubsitesLayer:IntegrationTesting',
)


KULEUVEN_SUBSITES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(KULEUVEN_SUBSITES_FIXTURE,),
    name='KuleuvenSubsitesLayer:FunctionalTesting',
)


KULEUVEN_SUBSITES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        KULEUVEN_SUBSITES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='KuleuvenSubsitesLayer:AcceptanceTesting',
)
