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
        
def heur_astar_test(problem_id, ref_id):

    s0 = PROBLEMS[problem_id]

    try:
        setTO(DEFAULT_TIMEOUT)

        a = iterative_astar(s0, heuristic=heur_alternate, weight=10, timebound=10)

        setTO(0)
        
        ref = REFERENCE[ref_id]
        
        if a == False:
            # Your A-star did not return a solution while it should
            assert False
            
        assert_almost_less_equal(ref[1], a.gval)
        if ref[3] != -1:
            assert_almost_less_equal(a.gval, ref[3])

    except TO_exc:
        print("Got TIMEOUT during problem {} when testing alternate heuristic".format(i))
        assert False
        
def test_p4_public_1b():
    heur_astar_test(13, 0)