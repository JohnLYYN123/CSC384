import pytest
import pickle

try:
    from planner import *
except ImportError:
    pass

from test_utils import *
from test_problems_public import PROBLEMS_PUBLIC as PROBLEMS

DEFAULT_TIMEOUT = 11

REFERENCE = pickle.load(open('test_ref_public.pickle', 'rb'))['p2']

def weighted_astar_test(problem_id, weight):

    s0 = PROBLEMS[problem_id]

    try:
        setTO(DEFAULT_TIMEOUT)

        a = weighted_astar(s0, heuristic=heur_manhattan_distance, weight=weight, timebound=10)

        setTO(0)
        
        ref = REFERENCE[problem_id][weight]
        
        if ref[0] == -1:
            return
        
        if a == False:
            # Your A-star did not return a solution while it should
            assert False
            
        assert_almost_equal(a.gval, ref[0])
        
        seq = a.get_action_sequence()
        assert_sequence_equal(seq, ref[1])

    except TO_exc:
        print("Got TIMEOUT during problem {} when testing weighted astar".format(i))
        assert False
            
def test_p2_public_1():
    weighted_astar_test(0, 1)

def test_p2_public_2():
    weighted_astar_test(0, 5)

def test_p2_public_3():
    weighted_astar_test(0, 10)

def test_p2_public_4():
    weighted_astar_test(0, 100)

def test_p2_public_5():
    weighted_astar_test(1, 1)

def test_p2_public_6():
    weighted_astar_test(1, 5)

def test_p2_public_7():
    weighted_astar_test(1, 10)

def test_p2_public_8():
    weighted_astar_test(1, 100)

def test_p2_public_9():
    weighted_astar_test(2, 1)

def test_p2_public_10():
    weighted_astar_test(2, 5)

def test_p2_public_11():
    weighted_astar_test(2, 10)

def test_p2_public_12():
    weighted_astar_test(2, 100)

def test_p2_public_13():
    weighted_astar_test(3, 1)

def test_p2_public_14():
    weighted_astar_test(3, 5)

def test_p2_public_15():
    weighted_astar_test(3, 10)

def test_p2_public_16():
    weighted_astar_test(3, 100)

def test_p2_public_17():
    weighted_astar_test(4, 1)

def test_p2_public_18():
    weighted_astar_test(4, 5)

def test_p2_public_19():
    weighted_astar_test(4, 10)

def test_p2_public_20():
    weighted_astar_test(4, 100)