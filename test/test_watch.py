import unittest
from mock import *

from pet import *
import pet
import pet.watch
import pet.perlre
import pet.exceptions

import re

class TestPetWatch(unittest.TestCase):

    def setUp(self):
        pass

    def test_watchrule_parse_on_perlre_compile_error(self):
        watchRule = pet.watch.WatchRule()
        rule = 'testrule1'
        pet.perlre.compile = MagicMock(side_effect=Exception())
        with self.assertRaises(pet.exceptions.InvalidWatchFile) as cm:
            watchRule.parse(rule)
        self.assertEquals(cm.exception.message,
                          "Rule '{0}' is invalid.".format(rule))

    def test_watchrule_parse_on_re_search_error(self):
        watchRule = pet.watch.WatchRule()
        rule = 'testrule2'
        re.search = MagicMock(side_effect=Exception())
        with self.assertRaises(pet.exceptions.InvalidWatchFile) as cm:
            watchRule.parse(rule)
        self.assertEquals(cm.exception.message,
                          "Rule '{0}' is invalid.".format(rule))

    # def test_watcher_checkrule_on_watchrule_uversionmangle_error(self):
    #     watcher = pet.watch.Watcher()
    #     watchRule = pet.watch.WatchRule()
    #     watchRule.parse('ok')
    #     pet.watch.WatchRule.uversionmangle = MagicMock(side_effect=TypeError())
    #     with self.assertRaises(pet.exceptions.InvalidVersion) as cm:
    #         watcher.check_rule(watchRule)
    #     self.assertEquals(cm.exception.message, "InvalidVersion")

