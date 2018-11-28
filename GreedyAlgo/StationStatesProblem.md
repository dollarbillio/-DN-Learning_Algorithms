## StationStatesProblem
**Problem**
* Given a collection of states, each can broadcast to a number of different states. Find a minimum number of stations that cover all of states
---
**Solution**
* Greedy Algorithm
1) Choose the ```bestStation``` that cover most states
2) Update the ```allStates``` to be covered by taking out the ```statesCovered``` by the ```bestStation```
3) Repeat 1) and 2) until there is no states to be covered
---
**Time Complexity**
* ```for loop``` inside a ```while loop```: O(n2)
---
**MAIN CODE**
```py
# convert list into set(no duplicates)
allStates = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# Create a set of stations to hold all stations that will be used to cover all states
finalStations = set()

while allStates:
    # Create the station that covers max states of all 
    bestStation = None
    # Creat a set of covered states
    statesCovered = set()

    # Loop all remaining stations to find the one that cover most states
    for station, linkedStates in stations.items():
        # Take the intersection between allStates available and linkedStates 
        # to find the station that covers most remain states
        toCover = allStates & linkedStates  
        if len(toCover) > len(statesCovered):
            # Set the best station as the one with most states covered
            bestStation = station
            # Update the maximum states covered by best station
            statesCovered = toCover
    
    # Add the current best station
    finalStations.add(bestStation)
    # Update so that there remaining only states that are not covered 
    allStates -= statesCovered    

print (finalStations) 
```
