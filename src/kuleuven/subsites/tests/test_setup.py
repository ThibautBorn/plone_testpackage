# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from kuleuven.subsites.testing import (
    KULEUVEN_SUBSITES_INTEGRATION_TESTING  # noqa: E501,
)
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that kuleuven.subsites is properly installed."""

    layer = KULEUVEN_SUBSITES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if kuleuven.subsites is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'kuleuven.subsites'))

    def test_browserlayer(self):
        """Test that IKuleuvenSubsitesLayer is registered."""
        from kuleuven.subsites.interfaces import (
            IKuleuvenSubsitesLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IKuleuvenSubsitesLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = KULEUVEN_SUBSITES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['kuleuven.subsites'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if kuleuven.subsites is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'kuleuven.subsites'))

    def test_browserlayer_removed(self):
        """Test that IKuleuvenSubsitesLayer is removed."""
        from kuleuven.subsites.interfaces import \
            IKuleuvenSubsitesLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IKuleuvenSubsitesLayer,
            utils.registered_layers())
