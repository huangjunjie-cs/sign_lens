#!/usr/bin/env python
"""Tests for `sign_lens` package."""
# pylint: disable=redefined-outer-name
import os
import unittest

from sign_lens import SignLens
from sign_lens import SignedTriadFeaExtra


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class TestSignedTriadFeaExtra(unittest.TestCase):

    def setUp(self) -> None:
        test_fpath = os.path.join(BASE_DIR, 'test_datas', 'simple-1.edgelist')
        self.model = SignedTriadFeaExtra(edgelist_fpath=test_fpath)


class TestSignLens(unittest.TestCase):

    def setUp(self) -> None:
        test_fpath = os.path.join(BASE_DIR, 'test_datas', 'bitcoin_alpha.edgelist')
        self.model = SignLens(edgelist_fpath=test_fpath)

    # def test_calc_edge_num(self):
    #     edge_num = self.model.calc_edge_num()
    #     self.assertEqual(edge_num, 24186)
    #     self.assertEqual(edge_num, len(self.model.G.edges))

    # def test_calc_node_num(self):
    #     node_num = self.model.calc_node_num()
    #     self.assertEqual(node_num, 3783)
    #     self.assertEqual(node_num, len(self.model.G.nodes))

    # def test_calc_sign_dist(self):
    #     pos_num, neg_num, ratio = self.model.calc_sign_dist()
    #     self.assertEqual(pos_num, len(self.model.pos_G.edges))
    #     self.assertEqual(neg_num, len(self.model.neg_G.edges))
    #     self.assertEqual( ratio * 100 // 1 / 100,  0.93)

    # def test_calc_signed_in_and_out_degree(self):
    #     G_in_degree, pos_G_in_degree, neg_G_in_degree = self.model.calc_signed_in_degree()
    #     G_out_degree, pos_G_out_degree, neg_G_out_degree = self.model.calc_signed_in_degree()
    #     in_degree_total = sum(G_in_degree.values())
    #     out_degree_total = sum(G_out_degree.values())
    #     self.assertEqual(in_degree_total, out_degree_total)

    #     neg_in_degree_total = sum(neg_G_in_degree.values())
    #     neg_out_degree_total = sum(neg_G_out_degree.values())
    #     self.assertEqual(neg_in_degree_total, neg_out_degree_total)

    #     pos_in_degree_total = sum(pos_G_in_degree.values())
    #     pos_out_degree_total = sum(pos_G_out_degree.values())
    #     self.assertEqual(pos_in_degree_total, pos_out_degree_total)

    # def test_calc_hop_dist(self):
    #     s = self.model.calc_hop_dist()
    #     v = s.values()
    #     print(np.histogram(v))

    # def test_calc_singular_value_dist(self):
    #     s1 = self.model.calc_singular_value_dist()
    #     import ipdb; ipdb.set_trace()

    # def test_calc_signed_triangle_dist(self):
    #     ratio = self.model.calc_balanced_triangle_dist()
    #     print(ratio)
    #     self.assertEqual(round(ratio[0], 4), 0.8805)
    #     self.assertEqual(round(ratio[1], 4), 0.1195)

    # def test_calc_balance_triads_dist(self):
    #     ratio = self.model.calc_balance_triads_dist()
    #     print(ratio)

    def test_report_signed_metrics(self):
        self.model.report_signed_metrics()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
