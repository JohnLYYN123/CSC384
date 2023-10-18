import pytest
import pickle

try:
    from planner import *
except ImportError:
    pass

from test_utils import *
from test_problems_public import PROBLEMS_PUBLIC as PROBLEMS

DEFAULT_TIMEOUT = 10

REFERENCE = pickle.load(open('test_ref_public.pickle', 'rb'))['p1']

def manhattan_test(problem_id):

    s0 = PROBLEMS[problem_id]

    try:
        setTO(DEFAULT_TIMEOUT)

        man_dist = heur_manhattan_distance(s0)

        setTO(0)

        assert_almost_equal(man_dist, REFERENCE[problem_id])

    except TO_exc:
        print("Got TIMEOUT during problem {} when testing manhattan distance".format(i))
        assert False
            

def test_p1_public_1():
    manhattan_test(0)

def test_p1_public_2():
    manhattan_test(1)

def test_p1_public_3():
    manhattan_test(2)

def test_p1_public_4():
    manhattan_test(3)

def test_p1_public_5():
    manhattan_test(4)

def test_p1_public_6():
    manhattan_test(5)

def test_p1_public_7():
    manhattan_test(6)

def test_p1_public_8():
    manhattan_test(7)

def test_p1_public_9():
    manhattan_test(8)

def test_p1_public_10():
    manhattan_test(9)

def test_p1_public_11():
    manhattan_test(10)

def test_p1_public_12():
    manhattan_test(11)

def test_p1_public_13():
    manhattan_test(12)

def test_p1_public_14():
    manhattan_test(13)

def test_p1_public_15():
    manhattan_test(14)

def test_p1_public_16():
    manhattan_test(15)

def test_p1_public_17():
    manhattan_test(16)

def test_p1_public_18():
    manhattan_test(17)

def test_p1_public_19():
    manhattan_test(18)

def test_p1_public_20():
    manhattan_test(19)