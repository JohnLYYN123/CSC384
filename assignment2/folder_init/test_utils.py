#Utilities
import signal
# import resource

# def containsList(lst):
#     '''true if lst contains lists'''
#     if not isinstance(lst, list):
#         return False
#     for e in lst:
#         if isinstance(e, list):
#             return True
#     return False
    
# def sortInnerMostLists(lst):
#     '''sort the innermost lists in a list of lists of lists...'''
#     if not isinstance(lst, list):
#         return
#     elif containsList(lst):
#         for e in lst:
#             sortInnerMostLists(e)
#     else:
#         lst.sort()

class TO_exc(Exception):
    pass

def toHandler(signum, frame):
    raise TO_exc()

def setTO(TOsec):
    signal.signal(signal.SIGALRM, toHandler)
    signal.alarm(TOsec)
    
def assert_almost_equal(a, b):
    # Extra min to conseal the correct answer
    assert min(0.01, abs(float(a)-float(b))) < 1e-5

def assert_sequence_equal(a, b):
    assert_almost_equal(len(a), len(b))
    for i in range(len(a)):
        assert a[i] == b[i]
        
def assert_almost_less_equal(a, b):
    assert max(-0.01, min(0.01, b-a)) >= -1e-5
    
# def setMEM(maxmem):
#     '''Sets a limit to virtual memory (in MB).
#     When something allocates beyond this limit, Python will raise a MemoryError
#     exception. The except block *must* delete some objects ASAP, anything else
#     might raise the exception again. 

#     This will (probably) not work on anything other than Linux (>=2.4). It
#     might also fail occasionally, as there are no guarantees that we can
#     recover from a memory error.
#     '''
#     rsrc = resource.RLIMIT_AS
#     _, hard = resource.getrlimit(rsrc)
    
#     soft = maxmem * 1024 * 1024
#     resource.setrlimit(rsrc,(soft,hard))

# def resetMEM():
#     rsrc = resource.RLIMIT_AS
#     _, hard = resource.getrlimit(rsrc)

#     resource.setrlimit(rsrc,(hard,hard))
