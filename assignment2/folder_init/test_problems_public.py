from warehouse import WarehouseState

PROBLEMS_PUBLIC = (
    WarehouseState("START", 0, None, 5, 5, # dimensions
                 ((2, 2),), #robots
                 frozenset(((1, 3),)), #boxes
                 frozenset(((4, 4),)), #storage
                 frozenset(((1, 0), (2, 0), (3, 0), (1, 4), (2, 4), (3, 4))) #obstacles
                 ),
    WarehouseState("START", 0, None, 6, 4, # dimensions
                 ((2, 1), (2, 2)), #robots
                 frozenset(((1, 1), (1, 2), (4, 1), (4, 2))), #boxes 
                 frozenset(((2, 1), (2, 2), (3, 1), (3, 2))), #storage
                 frozenset() #obstacles
                 ),
    WarehouseState("START", 0, None, 6, 4, # dimensions
                 ((2, 1),), #robots
                 frozenset(((1, 1), (1, 2), (4, 1))), #boxes 
                 frozenset(((2, 1), (3, 1), (3, 2))), #storage
                 frozenset() #obstacles
                 ),
    WarehouseState("START", 0, None, 6, 4, # dimensions
                 ((2, 1),), #robots
                 frozenset(((1, 1), (4, 2))), #boxes 
                 frozenset(((2, 1), (2, 2))), #storage
                 frozenset() #obstacles
                 ),
    WarehouseState("START", 0, None, 6, 4, # dimensions
                 ((2, 1),), #robots
                 frozenset(((4, 2),)), #boxes 
                 frozenset(((2, 1),)), #storage
                 frozenset() #obstacles
                 ),
    WarehouseState("START", 0, None, 5, 5, # dimensions
                 ((4, 0),), #robots
                 frozenset(((3, 1), (3, 2))), #boxes 
                 frozenset(((0, 0), (0, 2))), #storage
                 frozenset(((2, 0), (2, 1), (2, 3), (2, 4))) #obstacles
                 ),
    WarehouseState("START", 0, None, 6, 6, # dimensions
                 ((0, 0), (5, 1), (0, 2), (5, 3), (0, 4), (5, 5)), #robots
                 frozenset(((1, 0), (4, 1), (1, 2), (4, 3), (1, 4), (4, 5))), #boxes 
                 frozenset(((5, 0), (0, 1), (5, 2), (0, 3), (5, 4), (0, 5))), #storage
                 frozenset() #obstacles
                 ),
    WarehouseState("START", 0, None, 6, 6, # dimensions
                 ((5, 1), (0, 4)), #robots
                 frozenset(((1, 0), (4, 1), (1, 2), (4, 3), (1, 4), (4, 5))), #boxes 
                 frozenset(((5, 0), (0, 1), (5, 2), (0, 3), (5, 4), (0, 5))), #storage
                 frozenset() #obstacles
                 ),
    WarehouseState("START", 0, None, 6, 6, # dimensions
                 ((0, 2), (3, 3)), #robots
                 frozenset(((1, 0), (1, 2), (1, 4))), #boxes 
                 frozenset(((5, 0), (0, 3), (0, 5))), #storage
                 frozenset() #obstacles
                 ),
    WarehouseState("START", 0, None, 6, 6, # dimensions
                 ((0, 2), (3, 3)), #robots
                 frozenset(((1, 0), (1, 2), (1, 4))), #boxes 
                 frozenset(((5, 0), (0, 3), (5, 4))), #storage
                 frozenset() #obstacles
                 ),
    WarehouseState("START", 0, None, 6, 6,  # dimensions
                 ((5, 5), (5, 4), (4, 5)),  # robots
                 frozenset(((3, 1), (1, 4), (3, 4))),  # boxes
                 frozenset(((0, 0), (0, 1), (1, 0))),  # storage
                 frozenset()  # obstacles
                 ),
    WarehouseState("START", 0, None, 5, 5,  # dimensions
                 ((4, 0), (4, 4)),  # robots
                 frozenset(((3, 1), (3, 2), (3, 3))),  # boxes
                 frozenset(((0, 0), (0, 2), (0, 4))),  # storage
                 frozenset(((2, 0), (2, 1), (2, 3), (2, 4)))  # obstacles
                 ),
    WarehouseState("START", 0, None, 5, 5,  # dimensions
                 ((2, 1), (2, 3)),  # robots
                 frozenset(((1, 1), (1, 3), (3, 1), (3, 3))),  # boxes
                 frozenset(((0, 0), (0, 4), (4, 0), (4, 4))),  # storage
                 frozenset(((1, 0), (2, 0), (3, 0), (1, 4), (2, 4), (3, 4)))  # obstacles
                 ),
    WarehouseState("START", 0, None, 6, 6,  # dimensions nist
                 ((5, 5), (5, 4)),  # robots
                 frozenset(((3, 1), (2, 2), (1, 4))),  # boxes
                 frozenset(((0, 0), (0, 1), (1, 0))),  # storage
                 frozenset()  # obstacles
                 ),
    WarehouseState("START", 0, None, 8, 8, # dimensions
                 ((0, 5), (1, 6), (2, 7)), #robots
                 frozenset(((6, 4), (6, 6), (5, 6), (6, 1), (4, 5), (5, 2))), #boxes 
                 frozenset(((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2))), #storage
                 frozenset() #obstacles
                 ),
    WarehouseState("START", 0, None, 8, 8, # dimensions
                 ((0, 5), (1, 6)), #robots
                 frozenset(((4, 5), (5, 3), (4, 4), (6, 6))), #boxes 
                 frozenset(((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2))), #storage
                 frozenset() #obstacles
                 ),
    WarehouseState("START", 0, None, 8, 8, # dimensions
                 ((0, 5), (1, 6)), #robots
                 frozenset(((5, 6), (4, 4), (4, 3), (6, 5), (6, 2))), #boxes 
                 frozenset(((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2))), #storage
                 frozenset() #obstacles
                 ),
    WarehouseState("START", 0, None, 8, 8, # dimensions
                 ((0, 5), (1, 6)), #robots
                 frozenset(((6, 4), (6, 6), (5, 6), (6, 1), (4, 5), (5, 2))), #boxes 
                 frozenset(((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2))), #storage
                 frozenset() #obstacles
                 ),
    WarehouseState("START", 0, None, 8, 8,  # dimensions
                 ((0, 5), (1, 6), (2, 7)),  # robots
                 frozenset(((5, 4), (5, 5), (6, 3), (4, 2), (6, 5), (5, 3))),  # boxes
                 frozenset(((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2))),  # storage
                 frozenset()  # obstacles
                 ),
    WarehouseState("START", 0, None, 8, 8,  # dimensions
                 ((0, 5), (1, 6), (2, 7)),  # robots
                 frozenset(((6, 6), (4, 5), (4, 1), (4, 3), (5, 2), (5, 3))),  # boxes
                 frozenset(((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2))),  # storage
                 frozenset()  # obstacles
                 ),
    )
