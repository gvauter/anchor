# -*- coding:utf-8 -*-
#
# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import unittest
from anchor.app import ConfigValidationException
from anchor.app import validate_config

class TestValidDN(unittest.TestCase):
    test_bad_validator = [
        {
            "name": "default",
            "steps": [
                ('common_name', {'allowed_domains': ['badexample.com']}),
                ('alternative_names', {'allowed_domains': ['.example.com']})
            ]
        },
    ]

    test_good_validator = [
        {
            "name": "default",
            "steps": [
                ('common_name', {'allowed_domains': ['.example.com']}),
                ('alternative_names', {'allowed_domains': ['.example.com']})
            ]
        },
    ]


    def setUp(self):
        super(TestValidDN, self).setUp()

    def tearDown(self):
        pass

    def test_testing(self):
        self.assertTrue(True)

    def test_validate_config(self):
        self.assertRaises(ConfigValidationException, validate_config, TestValidDN.test_validator)

    def test_validate_config(self):
        validate_config(test_good_validator)