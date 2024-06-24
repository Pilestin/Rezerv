import sys

sys.path.append(r"E:/Kodlar/alnsesogutest_v4")

from AlnsObjects.Solution import Solution
from AlnsObjects.Route import Route
from DataObjects.ChargeStation import ChargeStation
from DataObjects.Customer import Customer
from DataObjects.Target import Target
from readProblemInstances import readProblemInstances

import xml.etree.ElementTree as ET
import numpy as np

file = r"E:\Kodlar\alnsesogutest_v4\SchneiderData\newesogu-r5-ds1.xml"
def array_to_solution(routes):
    
    tree = ET.parse(file)
    root = tree.getroot()
    distance_matrix_tag = 'DijkstraMatrix'
    distance_matrix_data = root.find(distance_matrix_tag).text
    matrix_lines = distance_matrix_data.splitlines()
    distance_matrix = np.array([[int(x) for x in line.split()] for line in matrix_lines])
    
    points = root.find("Points")
    total_solution = 0        
    
    for route in routes:
        left = None
        right = None
        route_solution = 0
        last_part = 0
        for index in range(1,len(route)):
            
            left = index-1 
            right = index
            
            for point in points:
                left_item = route[left].replace(" ", "")
                
                if point.attrib["Name"] == left_item :
                    left_index = int(point.attrib["No"]) - 1
                    
                right_item = route[right].replace(" ", "")
                if point.attrib["Name"] == right_item :
                    right_index = int(point.attrib["No"]) - 1    
                    
            print(f"{route[left]}({left_index}) - {route[right]}({right_index}) \t: {distance_matrix[left_index][right_index]}")        
            route_solution += distance_matrix[left_index][right_index]
            if "cs" in route[index]  :
                print("---------part----------", "+", route_solution, "  |  ", 3000 - (route_solution - last_part))
                last_part = route_solution    
                
        total_solution += route_solution

    print("Total Solution : ", total_solution)

def get_Solution(routes, problem_instance):
    
    unserved_customers = []
    served_customers = []

    solution = Solution(unserved_customers, served_customers, routes, problem_instance)
    return solution

def string_to_array(string_data):

    cleaned_data = string_data.strip("[]").replace("], ", "]|").split("|")
    final_data = [[item.strip(" '[]") for item in row.split(",")] for row in cleaned_data]

    return final_data
# [[cs5, 60A/2, 75, cs3, 31, 32, cs6, 19, cs2, cs5 ]] 
# [CS5-32-19-CS6-31-60A/2-75-CS3-CS5]
# my_solution = "[cs5, 32, 19, cs6, 31, 60A/2, 75, cs3, cs5 ]" 
my_solution = "[[cs5, 32, 19, 31, cs4, 60A/2, 75, cs3,  cs5, ]]"
my_solution = string_to_array(my_solution)
print(my_solution)
array_to_solution(my_solution)

