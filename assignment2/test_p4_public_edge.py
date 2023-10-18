import pytest
import pickle

try:
    from planner import *
except ImportError:
    pass

from test_utils import *
from test_problems_public import PROBLEMS_PUBLIC as PROBLEMS
        
def test_p4_edge():
    s0 = WarehouseState("START", 0, None, 5, 5, # dimensions
                 ((4, 2),), #robots
                 frozenset(((4, 3),)), #boxes
                 frozenset(((4, 4),)), #storage
                 frozenset(((1, 0), (2, 0), (3, 0), (1, 4), (2, 4), (3, 4))) #obstacles
                 )
    
    d = heur_alternate(s0)
    assert_almost_equal(1, d)