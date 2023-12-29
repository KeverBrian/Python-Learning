import numpy as np
import pandas as pd

TSP = pd.read_excel(r'C:\Users\linji\OneDrive\桌面\python\excel\TravelSalersProblem.xlsx',header=None)
TSP = np.array(TSP)

cities = list(range(TSP.shape[0]-1))
distances = TSP[1:, 1:]

#临近算法
def nearest_neighbor(distances, start_city):
    # 初始化
    unvisited_cities = set(cities)
    unvisited_cities.remove(start_city)
    forcities = set(unvisited_cities)
    dict_tour = {}
    for i in forcities:
        current_city = i
        tour = [start_city]
        tour_distance = 0
        unvisited_cities = set(forcities)
        unvisited_cities.remove(current_city)
        tour.append(current_city)
    # 逐步访问
        while unvisited_cities:
            next_city = min(unvisited_cities, key=lambda city: distances[current_city][city])
            unvisited_cities.remove(next_city)
            tour.append(next_city)
            tour_distance += distances[current_city][next_city]
            current_city = next_city
        tour.append(start_city)
        tour_distance += distances[current_city][start_city]
        dict_tour[i] = [tour,tour_distance]
    min_tour = min(dict_tour.items(), key=lambda item: item[1][1])[0]
    return dict_tour[min_tour]

#二临近算法
def nearest_twoneighbors(distances, start_city):
    # 初始化
    tour = [start_city]
    tour_distance = 0
    unvisited_cities = set(cities)
    unvisited_cities.remove(start_city)
    current_city = start_city
    # 逐步访问
    while unvisited_cities:
        next_twocities = min(unvisited_cities, key=lambda city: distances[current_city][city]+min(distances[city]))
        unvisited_cities.remove(next_twocities)
        tour.append(next_twocities)
        tour_distance += distances[current_city][next_twocities]
        current_city = next_twocities
    tour.append(start_city)
    tour_distance += distances[current_city][start_city]
    return tour, tour_distance

#使用临近算法
tour1 = nearest_neighbor(distances, 0)[0]
tour1_distance = nearest_neighbor(distances, 0)[1]
print("Tour_One:", tour1, "Total distance:", tour1_distance)

#使用二临近算法
#tour2 = nearest_twoneighbors(distances, 0)[0]
#tour2_distance = nearest_twoneighbors(distances, 0)[1]
#print("Tour_Two:", tour2, "Total distance:", tour2_distance)