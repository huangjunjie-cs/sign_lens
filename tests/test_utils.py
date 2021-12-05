#!/usr/bin/env python
"""Tests for `sign_lens` package."""
# pylint: disable=redefined-outer-name
import os
import unittest

from sign_lens.utils import SignedTriadFeaExtra, SignedTriadFeaExtraByMatrce


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class TestSignedTriadFeaExtraByMatrce(unittest.TestCase):

    def setUp(self) -> None:
        test_fpath = os.path.join(BASE_DIR, 'test_datas', 'simple_case.edgelist')
        test_fpath = os.path.join(BASE_DIR, 'test_datas', 'bitcoin_alpha.edgelist')
        test_fpath = os.path.join(BASE_DIR, 'test_datas', 'bitcoin_otc.edgelist')
        self.model1 = SignedTriadFeaExtra(edgelist_fpath=test_fpath)
        self.model2 = SignedTriadFeaExtraByMatrce(edgelist_fpath=test_fpath)

    def test_balanced_theory(self):
        s01, s11, s21, s31 = self.model1.calc_balance_and_status_triads_num()

        s02, s12, s22, s32 = self.model2.calc_balance_and_status_triads_num()

        self.assertEqual(s01, s02)
        self.assertEqual(s11, s12)
        self.assertEqual(s21, s22)
        self.assertEqual(s31, s32)