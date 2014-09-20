import doctest
import unittest

from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
from Products.PloneTestCase.layer import onsetup

import mingtak.loginmethod

OPTION_FLAGS = doctest.NORMALIZE_WHITESPACE | \
               doctest.ELLIPSIS

ptc.setupPloneSite(products=['mingtak.loginmethod'])


class TestCase(ptc.PloneTestCase):

    class layer(PloneSite):

        @classmethod
        def setUp(cls):
            zcml.load_config('configure.zcml',
              mingtak.loginmethod)

        @classmethod
        def tearDown(cls):
            pass


def test_suite():
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='mingtak.loginmethod',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='mingtak.loginmethod.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        ztc.ZopeDocFileSuite(
            'INTEGRATION.txt',
            package='mingtak.loginmethod',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),

        # -*- extra stuff goes here -*-

        # Integration tests for LoginMethod
        ztc.ZopeDocFileSuite(
            'LoginMethod.txt',
            package='mingtak.loginmethod',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
