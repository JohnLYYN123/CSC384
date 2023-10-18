#!/bin/bash

! python3.9 -m pytest test_p1_public.py
! python3.9 -m pytest test_p2_public.py
! python3.9 -m pytest test_p3_public.py
! python3.9 -m pytest test_p4_public_edge.py
! python3.9 -m pytest test_p4_public_dist.py
! python3.9 -m pytest test_p4_public_steps.py