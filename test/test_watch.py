import unittest
from mock import *

from pet import *
import pet
import pet.watch
import pet.perlre
import pet.exceptions

import urllib2
import StringIO
import re

class TestPetWatch(unittest.TestCase):

    def setUp(self):
        self.watchRule = pet.watch.WatchRule()
        self.watcher = pet.watch.Watcher()
        self.cpan = pet.watch.CPAN()

    def test_timeout(self):
        self.assertEquals(180, pet.watch.TIMEOUT())

    def test_watchrule_parse_on_perlre_compile_error(self):
        rule = 'testrule1'
        pet.perlre.compile = MagicMock(side_effect=Exception())
        with self.assertRaises(pet.exceptions.InvalidWatchFile) as cm:
            self.watchRule.parse(rule)
        self.assertEquals("Rule '{0}' is invalid.".format(rule),
                          cm.exception.message)

    def test_watchrule_parse_on_re_search_error(self):
        rule = 'testrule2'
        re.search = MagicMock(side_effect=Exception())
        with self.assertRaises(pet.exceptions.InvalidWatchFile) as cm:
            self.watchRule.parse(rule)
        self.assertEquals("Rule '{0}' is invalid.".format(rule),
                          cm.exception.message)

    def test_cpan_init(self):
        self.assertEqual('ftp://ftp.cs.uu.nl/pub/CPAN/', self.cpan.mirror)
        self.assertIsNone(self.cpan._dists)
        self.assertIsNone(self.cpan._files)

    def test_cpan_dists_not_none(self):
        value = 'distscpantest1'
        self.cpan._dists = value
        self.assertEqual(value, self.cpan.dists)

    def test_cpan_dists_is_none_big_fields(self):
        entry1 = ["CGI::Header", "0.63", "A/AN/ANAZAWA/CGI-Header-0.63.tar.gz"]
        entry2 = ["Severo::Daniel", "7.63", "Z/ZZ/ZZOITDBEM/Severo-Daniel-7.63.tar.gz"]
        entry3 = ["Alienware::Satellite", "5.41", "D/DY/DYLAN/Alienware-Satellite-5.41.tar.gz"]
        entry_invalid = ["a", "b", "c42", "A/AB/ABC/a-b-c42.tar.gz"]
        contents_mock = [
            entry1[0] + "   " + entry1[1] + "   " + entry1[2],
            entry2[0] + "   " + entry2[1] + "   " + entry2[2],
            entry3[0] + "   " + entry3[1] + "   " + entry3[2],
            entry_invalid[0] + "   " + entry_invalid[1] + "   " + entry_invalid[2]
        ]
        self.cpan._get_and_uncompress = MagicMock(return_value=contents_mock)
        # MOCK StringIO close method to do nothing
        expected = [entry1[2], entry2[2], entry3[2]]
        actual = self.cpan.dists
        self.assertEqual(expected, actual)

    # def test_watcher_checkrule_on_watchrule_uversionmangle_error(self):
    #     self.watchRule.parse('run ./update-watch to find out what is a rule')
    #     pet.watch.WatchRule.uversionmangle = MagicMock(side_effect=TypeError())
    #     with self.assertRaises(pet.exceptions.InvalidVersion) as cm:
    #         self.watcher.check_rule(self.watchRule)
    #     self.assertEquals(cm.exception.message, "InvalidVersion")

    # def test_urlopen(self):
    #     urllib2.urlopen = MagicMock(return_value=666)
    #     kwargs = {"arg1":123, "int":"numero"}
    #     self.assertNotIn('context', arg1=123, int="numero")
    #     result = pet.watch.urlopen([1, 2, 3], kwargs)
    #     self.assertIn('context', kwargs)

