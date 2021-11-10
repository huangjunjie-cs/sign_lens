
import os
import numpy as np
from collections import defaultdict

class SignedTriadFeaExtra(object):

    def __init__(self, edgelist_fpath, undirected=False, seperator='\t'):
        self.undirected = undirected
        self.seperator = seperator

        res = self.init_edgelists(edgelist_fpath)
        self.pos_in_edgelists, self.pos_out_edgelists, self.neg_in_edgelists, self.neg_out_edgelists = res

    def init_edgelists(self, edgelist_fpath):
        pos_out_edgelists = defaultdict(list)
        neg_out_edgelists = defaultdict(list)
        pos_in_edgelists  = defaultdict(list)
        neg_in_edgelists  = defaultdict(list)
        with open(edgelist_fpath) as f:
            for line in f.readlines():
                x, y, z = line.split(self.seperator)
                x = int(x)
                y = int(y)
                z = int(z)
                if z == 1:
                    pos_out_edgelists[x].append(y)
                    pos_in_edgelists[y].append(x)
                else:
                    neg_out_edgelists[x].append(y)
                    neg_in_edgelists[y].append(x)

                if self.undirected:
                    # if undireced, repeat it
                    x, y = y, x
                    if z == 1:
                        pos_out_edgelists[x].append(y)
                        pos_in_edgelists[y].append(x)
                    else:
                        neg_out_edgelists[x].append(y)
                        neg_in_edgelists[y].append(x)

        return pos_in_edgelists, pos_out_edgelists, neg_in_edgelists, neg_out_edgelists

    def get_pos_indegree(self, v):
        return len(self.pos_in_edgelists[v])

    def get_pos_outdegree(self, v):
        return len(self.pos_out_edgelists[v])

    def get_neg_indegree(self, v):
        return len(self.neg_in_edgelists[v])

    def get_neg_outdegree(self, v):
        return len(self.neg_out_edgelists[v])

    def common_neighbors(self, u, v):
        u_neighbors = self.pos_in_edgelists[u] + self.neg_in_edgelists[u] + \
                      self.pos_out_edgelists[u] + self.neg_out_edgelists[u]
        v_neighbors = self.pos_in_edgelists[v] + self.neg_in_edgelists[v] + \
                      self.pos_out_edgelists[v] + self.neg_out_edgelists[v]
        return len(set(u_neighbors).intersection(set(v_neighbors)))


    def extract_triad_counts(self, u, v) -> tuple:
        """
        ++ +- -+ --
        ++ +- -+ --
        ++ +- -+ --
        ++ +- -+ --
        """
        d1_1 = len(set(self.pos_out_edgelists[u]).intersection(set(self.pos_in_edgelists[v])))
        d1_2 = len(set(self.pos_out_edgelists[u]).intersection(set(self.neg_in_edgelists[v])))
        d1_3 = len(set(self.neg_out_edgelists[u]).intersection(set(self.pos_in_edgelists[v])))
        d1_4 = len(set(self.neg_out_edgelists[u]).intersection(set(self.neg_in_edgelists[v])))

        d2_1 = len(set(self.pos_out_edgelists[u]).intersection(set(self.pos_out_edgelists[v])))
        d2_2 = len(set(self.pos_out_edgelists[u]).intersection(set(self.neg_out_edgelists[v])))
        d2_3 = len(set(self.neg_out_edgelists[u]).intersection(set(self.pos_out_edgelists[v])))
        d2_4 = len(set(self.neg_out_edgelists[u]).intersection(set(self.neg_out_edgelists[v])))

        d3_1 = len(set(self.pos_in_edgelists[u]).intersection(set(self.pos_out_edgelists[v])))
        d3_2 = len(set(self.pos_in_edgelists[u]).intersection(set(self.neg_out_edgelists[v])))
        d3_3 = len(set(self.neg_in_edgelists[u]).intersection(set(self.pos_out_edgelists[v])))
        d3_4 = len(set(self.neg_in_edgelists[u]).intersection(set(self.neg_out_edgelists[v])))

        d4_1 = len(set(self.pos_in_edgelists[u]).intersection(set(self.pos_in_edgelists[v])))
        d4_2 = len(set(self.pos_in_edgelists[u]).intersection(set(self.neg_in_edgelists[v])))
        d4_3 = len(set(self.neg_in_edgelists[u]).intersection(set(self.pos_in_edgelists[v])))
        d4_4 = len(set(self.neg_in_edgelists[u]).intersection(set(self.neg_in_edgelists[v])))

        return d1_1, d1_2, d1_3, d1_4, d2_1, d2_2, d2_3, d2_4, d3_1, d3_2, d3_3, d3_4, d4_1, d4_2, d4_3, d4_4

    def calc_balance_triads_num(self):
        s0, s1, s2, s3 = self.calc_balance_and_status_triads_num()
        return s1  + s2, s0

    def calc_balance_triads_dist(self):
        t1 = [] # +++ 
        t2 = [] # ++-
        t3 = [] # +--
        t4 = [] # ---
        for x in list(self.pos_out_edgelists):
            for y in self.pos_out_edgelists[x]:
                mask1 = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0] # +++ 
                mask2 = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0] #  ++- 
                mask3 = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1] #  +--
                mask4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #  ---
                rs = self.extract_triad_counts(x, y)
                t1.append(np.dot(mask1, rs))
                t2.append(np.dot(mask2, rs))
                t3.append(np.dot(mask3, rs))
                t4.append(np.dot(mask4, rs))

        for x in list(self.neg_out_edgelists):
            for y in self.neg_out_edgelists[x]:
                mask1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # +++ 
                mask2 = [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0] #  ++- 
                mask3 = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0] #  +--
                mask4 = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1] #  ---
                rs = self.extract_triad_counts(x, y)
                t1.append(np.dot(mask1, rs))
                t2.append(np.dot(mask2, rs))
                t3.append(np.dot(mask3, rs))
                t4.append(np.dot(mask4, rs))

        s1 = np.sum(t1)
        s2 = np.sum(t2)
        s3 = np.sum(t3)
        s4 = np.sum(t4)
        res = np.array([s1, s2, s3, s4]) 

        return  res / res.sum()


    def calc_balance_and_status_triads_num(self):
        rs0 = []
        rs1 = []
        rs2 = []
        rs3 = []
        for x in list(self.pos_out_edgelists):
            for y in self.pos_out_edgelists[x]:
                mask1 = [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1] # both satify
                mask2 = [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0] # only balance
                mask3 = [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0] # only status
                rs = self.extract_triad_counts(x, y)
                rs0.append(rs)
                rs1.append(np.dot(mask1, rs))
                rs2.append(np.dot(mask2, rs))
                rs3.append(np.dot(mask3, rs))

        for x in list(self.neg_out_edgelists):
            for y in self.neg_out_edgelists[x]:
                mask1 = [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0]
                mask2 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
                mask3 = [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1]
                rs = self.extract_triad_counts(x, y)
                rs0.append(rs)
                rs1.append(np.dot(mask1, rs))
                rs2.append(np.dot(mask2, rs))
                rs3.append(np.dot(mask3, rs))

        s0 = np.sum(rs0)
        s1 = np.sum(rs1)
        s2 = np.sum(rs2)
        s3 = np.sum(rs3)
        print('all triangle', s0)
        print('both', s1, s1/ s0)
        print('balance', s2, s2/ s0)
        print('status', s3, s3/ s0)
        return s0, s1, s2, s3
        

class FrustrationIndex:
    pass



if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    test_fpath = os.path.abspath(os.path.join(BASE_DIR, '..', 'tests', 'test_datas', 'simple_case.edgelist'))
    model = SignedTriadFeaExtra(edgelist_fpath=test_fpath)
    model.calc_balance_and_status_triads_num()