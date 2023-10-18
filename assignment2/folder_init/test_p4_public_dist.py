import pytest
import pickle

try:
    from planner import *
except ImportError:
    pass

from test_utils import *
from test_problems_public import PROBLEMS_PUBLIC as PROBLEMS

DEFAULT_TIMEOUT = 11

REFERENCE = pickle.load(open('test_ref_public.pickle', 'rb'))['p4']

def heur_better_than_md_test(problem_id, ref_id):

    s0 = PROBLEMS[problem_id]

    try:
        setTO(DEFAULT_TIMEOUT)

        d = heur_alternate(s0)

        setTO(0)
        
        ref = REFERENCE[ref_id]
            
        assert_almost_less_equal(ref[0]+1, d)
        assert_almost_less_equal(d, ref[2])

    except TO_exc:
        print("Got TIMEOUT during problem {} when testing alternate heuristic".format(i))
        assert False
            
def test_p4_public_1a():
    heur_better_than_md_test(13, 0)