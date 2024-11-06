# the set-covering problem: given a number of radio stations and the states they play at,
# pick the lowest number (smallest set) of radio stations such that all states are covered.

# Greedy approach:
# 1. pick the station that covers the most states that haven't been covered yet
# 2. repeat until all states are covered


def best_stations(states_needed:set, stations:dict) -> set:
    final_stations = set()

    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            # get the states this radio station covers that are 
            # in the needed states
            covered = states_needed & states_for_station
            
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        states_needed -= states_covered
        final_stations.add(best_station)
    
    return final_stations



states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}

stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
    
print(best_stations(states_needed, stations))
