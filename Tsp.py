import numpy as np
import pandas as pd
import random
import heapq

TSP = pd.read_excel(r'C:\Users\linji\OneDrive\桌面\python\excel\TravelSalersProblem.xlsx',header=None)
TSP = np.array(TSP)

cities = list(range(TSP.shape[0]-1))
distances = TSP[1:, 1:]
#print("distances:", distances)

#临近算法
def nearest_neighbor(distances, start_city):
    # 初始化
    forcities = set(cities)
    forcities.remove(start_city)
    dict_tour = {}
    #循环每个邻居城市
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
    if len(dict_tour) == 0:
        return [start_city,0]
    else:
        min_tour = min(dict_tour.items(), key=lambda item: item[1][1])[0]
        return dict_tour[min_tour]

#二临近算法(和临近算法相同结果)
def nearest_twoneighbors(distances, start_city):
    # 初始化
    forcities = set(cities)
    forcities.remove(start_city)
    dict_tour = {}
    #循环每个邻居城市
    for i in forcities:
        current_city = i
        tour = [start_city]
        tour_distance = 0
        unvisited_cities = set(forcities)
        unvisited_cities.remove(current_city)
        tour.append(current_city)
    # 逐步访问
        while unvisited_cities:
            next_city = min(unvisited_cities, key=lambda city: distances[current_city][city]+min([i for i in distances[city] if i != 0 and i != min(distances[city])]))
            unvisited_cities.remove(next_city)
            tour.append(next_city)
            tour_distance += distances[current_city][next_city]
            current_city = next_city
        tour.append(start_city)
        tour_distance += distances[current_city][start_city]
        dict_tour[i] = [tour,tour_distance]
    if len(dict_tour) == 0:
        return [start_city,0]
    else:
        min_tour = min(dict_tour.items(), key=lambda item: item[1][1])[0]
        return dict_tour[min_tour]

#相对距离算法(和临近算法相同结果)
def relative_neighbors(distances, start_city):
    # 初始化
    forcities = set(cities)
    forcities.remove(start_city)
    dict_tour = {}
    mean_dist = np.array([[i[0],np.mean(i[1:])] for i in TSP[1:]]) #计算每个城市到其他城市的平均距离
    for i in forcities:
        current_city = i
        tour = [start_city]
        tour_distance = 0
        unvisited_cities = set(forcities)
        unvisited_cities.remove(current_city)
        tour.append(current_city)
    # 逐步访问
        while unvisited_cities:
            next_city = min(unvisited_cities, key=lambda city: distances[current_city][city]/float(mean_dist[city][1]))
            unvisited_cities.remove(next_city)
            tour.append(next_city)
            tour_distance += distances[current_city][next_city]
            current_city = next_city
        tour.append(start_city)
        tour_distance += distances[current_city][start_city]
        dict_tour[i] = [tour,tour_distance]
    min_tour = min(dict_tour.items(), key=lambda item: item[1][1])[0]
    return dict_tour[min_tour]

#重复临近算法(失败品)
def renearest_neighbor(distances, start_city):
    # 初始化
    global cities
    tour = [start_city]
    tour_distance = 0
    recity = nearest_neighbor(distances, start_city)[0][1]
    tour_distance += distances[start_city][recity]
    cities.remove(start_city)
    # 逐步访问
    while cities:
        ntour = nearest_neighbor(distances, recity)[0]
        tour.append(recity)
        cities.remove(recity)
        if type(ntour) == int:
            break
        else:
            tour_distance += distances[recity][ntour[1]]
            recity = ntour[1]
    tour.append(start_city)
    tour_distance += distances[recity][start_city]
    cities = list(range(TSP.shape[0]-1))
    return tour, tour_distance

#随机算法
def random_tour(distances,start_city,times):
    min_tour = []
    min_distance =0
    for t in range(times):
        tour = [start_city]
        current_city = start_city
        tour_distance = 0
        forcities = list(cities)
        forcities.remove(start_city)
        while forcities:
            random_next = random.choice(forcities)
            tour.append(random_next)
            tour_distance += distances[current_city][random_next]
            forcities.remove(random_next)
            current_city = random_next
        tour.append(start_city)
        tour_distance += distances[current_city][start_city]
        if min_distance == 0 or min_distance > tour_distance:
            min_distance = tour_distance
            min_tour = tour
        else:
            pass
    return min_tour, min_distance

#使用临近算法
tour1 = nearest_neighbor(distances, 0)
print("Tour_One:", tour1[0], "Total distance:", tour1[1])

#使用二临近算法
tour2 = nearest_twoneighbors(distances, 0)
print("Tour_Two:", tour2[0], "Total distance:", tour2[1])

#使用相对距离算法
tour3 = relative_neighbors(distances, 0)
print("Tour_Three:", tour3[0], "Total distance:", tour3[1])

#使用重复临近算法
tour4 = renearest_neighbor(distances, 0)
print("Tour_Four:", tour4[0], "Total distance:", tour4[1])

#使用随机算法
tour5 = random_tour(distances,0,2000)
print("Tour_Five:", tour5[0], "Total distance:", tour5[1])