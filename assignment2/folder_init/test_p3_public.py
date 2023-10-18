import pytest
import pickle

try:
    from planner import *
except ImportError:
    pass

from test_utils import *
from test_problems_public import PROBLEMS_PUBLIC as PROBLEMS

DEFAULT_TIMEOUT = 11

REFERENCE = pickle.load(open('test_ref_public.pickle', 'rb'))['p3']

def iterative_astar_test(problem_id):

    s0 = PROBLEMS[problem_id]

    try:
        setTO(DEFAULT_TIMEOUT)

        a = iterative_astar(s0, heuristic=heur_manhattan_distance, weight=10, timebound=10)

        setTO(0)
        
        ref = REFERENCE[problem_id]
        
        if ref[0] == -1:
            return
        
        if a == False:
            # Your A-star did not return a solution while it should
            assert False
            
        assert_almost_less_equal(a.gval, ref[0])
        
        if ref[1] != False:
            assert_almost_less_equal(ref[1], a.gval)

    except TO_exc:
        print("Got TIMEOUT during problem {} when testing iterative astar".format(problem_id))
        assert False
            
def test_p3_public_1():
    iterative_astar_test(0)

def test_p3_public_2():
    iterative_astar_test(1)

def test_p3_public_3():
    iterative_astar_test(2)

def test_p3_public_4():
    iterative_astar_test(3)

def test_p3_public_5():
    iterative_astar_test(4)

def test_p3_public_6():
    iterative_astar_test(5)

def test_p3_public_7():
    iterative_astar_test(6)

def test_p3_public_8():
    iterative_astar_test(7)

def test_p3_public_9():
    iterative_astar_test(8)

def test_p3_public_10():
    iterative_astar_test(9)