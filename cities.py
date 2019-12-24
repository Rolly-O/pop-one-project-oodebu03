import random
import copy

def read_cities(file_name):
    infile=open(file_name,"r")
    line=infile.readline()
    roadmap=[]
    while line!="":
       line.rstrip()
       mapplaces=line.split()
       roadmap.append((mapplaces[0],mapplaces[1],int(mapplaces[2]),int(mapplaces[4])))
       line=infile.readline()
    infile.close()

    #amend the roadmap list to have alabama at the end as well as the start
    #the item after lst[i] is not just lst(i + 1), but is lst[(i + 1) % len(lst)]
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 
      [(state, city, latitude, longitude), ...] 
    Use this as your initial `road_map`, that is, the cycle 
      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
  
def print_cities(road_map):
    for x in road_map:
        print(x[0]+" "+x[1]+" "+str(round(x[2],2))+" "+str(round(x[3],2)))

    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """

def compute_total_distance(road_map):
    dist=0
    # distance calc sqrt((x1-x2)^2 + (y1-y2)^2)
    #need to figure out how to get x1 and x2 - maybe call i in range for index
    #set x1 and y1 equal to i index and x2 and y2 equal to i+1
    #then do the distance calculation for then and recurse until at end of list
    #add to dist
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    return 0


def swap_cities(road_map, index1, index2):
    new_road_map=copy.copy(road_map)
    if index1==index2:
        pass
    else:
        new_road_map[index1]=road_map[index2]
        new_road_map[index2]=road_map[index1]

    new_total_distance = compute_total_distance(new_road_map)
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 
        (new_road_map, new_total_distance)
    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    return (new_road_map,new_total_distance)

def shift_cities(road_map):
    shiftmap=copy.copy(road_map)
    for i in range(0,length(road_map)):
        if i=length(road_map):
            shiftmap[i]=road_map[0]
        else:
            shiftmap[i]=road_map[i+1]
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    return shiftmap

def find_best_cycle(road_map):
    count=0
    while count<10000:
        N=2
        number = N * random.random()  #will give random num betw 0 and N
        if number==1:
            swap_cities(road_map)
        else:
            shift_cities(road_map)
        count=count+1
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    pass

def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    #cost for each connectin is distance of each connection and tot cost is tot distance
    pass

def visualise(road_map):
    """
    Need to figure out a way to visualise the road_map!!!!!!!!!!!!!!
    """

def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    filename=input("Please input the file name:")
    #does a combination of read_cities, find_best_cycle then print_map for this
    #once others are done then can just
    read_cities(filename)
    return print_cities(road_map)
    m=find_best_cycle(road_map)
    return m
    return visualise(m)

if __name__ == "__main__": #keep this in
    main()
