import pytest
from cities import *

def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

    '''add your further tests'''
    assert not compute_total_distance(road_map1)==0 #stub
    assert not compute_total_distance(road_map1)==\
           pytest.approx(88.098+337.103+113.347, 0.01) #missing sqrt
    assert not compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496, 0.01) #not circular list so missing the last sum

def test_swap_cities():
    '''add your tests'''
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    road_map2 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Minnesota", "Saint Paul", 44.95, -93.094),\
                ("Delaware", "Dover", 39.161921, -75.526755)]
    assert not test_swap_cities(road_map1,1,2)==road_map1
    assert test_swap_cities(roadmap1,1,2)==road_map2
    assert test_swap_cities(roadmap1,1,1)==road_map1
    #want to test the indices provided are not out of scope
    

def test_shift_cities():
    '''add your tests'''
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    road_map2 = [("Minnesota", "Saint Paul", 44.95, -93.094),\
                ("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755)]
    assert not test_shift_cities(road_map1)==road_map1
    assert test_shift_cities(road_map1)==road_map2
    #want to test there is no error in the running of the func
    


