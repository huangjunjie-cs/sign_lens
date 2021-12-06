#!/usr/bin/env python
"""Tests for `sign_lens` package."""
# pylint: disable=redefined-outer-name
import os
import unittest
from unittest.case import expectedFailure

from sign_lens import SignBipartiteLens
from sign_lens import SignedBipartiteFeaExtra, SignedBipartiteFeaExtraByMatrace

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# class TestSignedTriadFeaExtra(unittest.TestCase):

#     def setUp(self) -> None:
#         test_fpath = os.path.join(BASE_DIR, 'test_datas', 'senate1to10.edgelist')
#         test_fpath = os.path.join(BASE_DIR, 'test_datas', 'bipartite_test.edgelist')
#         self.model1 = SignedBipartiteFeaExtra(edgelist_fpath=test_fpath)
#         self.model2 = SignedBipartiteFeaExtraByMatrace(edgelist_fpath=test_fpath)

#     def test_balanced_theory(self):
#         _, res2 = self.model2.calc_signed_bipartite_butterfly_dist()
#         print(res2)
#         _, res1 = self.model1.calc_signed_bipartite_butterfly_dist()

#         self.assertEqual(len(res1), len(res2))

#         for i, j in zip(res1, res2):
#             print(i, j)
#             self.assertEqual(i, j)



class TestSignBipartiteLens(unittest.TestCase):
    def setUp(self) -> None:
        test_fpath = os.path.join(BASE_DIR, 'test_datas',
                                  'senate1to10.edgelist')
        self.model = SignBipartiteLens(edgelist_fpath=test_fpath)

    def test_calc_node_num(self):
        node_num1, node_num2 = self.model.calc_node_num()
        self.assertEqual(node_num1, 145)
        self.assertEqual(node_num2, 1056)

    def test_calc_edge_num(self):
        edge_num = self.model.calc_edge_num()
        self.assertEqual(edge_num, 27083)

    def test_calc_signed_bipartite_butterfly_dist(self):
        exceptation_res = [
            0.262,  # ++++
            0.108,  # +--+
            0.110,  # ++--
            0.184,  # +-+-
            0.133,  # ----
            0.122,  # +++-
            0.081   # +---
        ]
        _, res = self.model.calc_signed_bipartite_butterfly_dist()
        self.assertEqual(len(res), len(exceptation_res))
        for i, j in zip(exceptation_res, res):
            self.assertEqual(i, round(j, 3))

    def test_report_signe_metrics(self):
        self.model.report_signed_metrics()

if __name__ == '__main__':
    unittest.main()
