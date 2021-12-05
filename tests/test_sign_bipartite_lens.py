#!/usr/bin/env python
"""Tests for `sign_lens` package."""
# pylint: disable=redefined-outer-name
import os
import unittest
from unittest.case import expectedFailure

from sign_lens import SignBipartiteLens

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# class TestSignBipartiteLens(unittest.TestCase):
#     def setUp(self) -> None:
#         test_fpath = os.path.join(BASE_DIR, 'test_datas',
#                                   'senate1to10.edgelist')
#         self.model = SignBipartiteLens(edgelist_fpath=test_fpath)

#     def test_calc_node_num(self):
#         node_num1, node_num2 = self.model.calc_node_num()
#         self.assertEqual(node_num1, 1056)
#         self.assertEqual(node_num2, 145)

#     def test_calc_edge_num(self):
#         edge_num = self.model.calc_edge_num()
#         self.assertEqual(edge_num, 27083)

#     def test_calc_signed_bipartite_butterfly_dist(self):
#         exceptation_res = [
#             0.262,  # ++++
#             0.108,  # +--+
#             0.110,  # ++--
#             0.184,  # +-+-
#             0.133,  # ----
#             0.122,  # +++-
#             0.081   # +---
#         ]
#         res = self.model.calc_signed_bipartite_butterfly_dist()
#         self.assertEqual(len(res), len(exceptation_res))
#         for i, j in zip(exceptation_res, res):
#             self.assertEqual(i, round(j, 3))


# if __name__ == '__main__':
#     unittest.main()
