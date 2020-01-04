import random
import copy

def read_cities(file_name):
    infile=open(file_name,"r")
    line=infile.readline()
    roadlist=[]
    while line!="":
       line.rstrip()
       mapplaces=line.split()
       roadlist.append((mapplaces[0],mapplaces[1],int(mapplaces[2]),int(mapplaces[3])))
       line=infile.readline()
    infile.close()

    road_map=[]
    while i<=len(roadlist):
        road_map[i]=roadlist[i]
    road_map[len(roadlist)+1]=roadlist[0]
    
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
    loc=[]
    for x in road_map:
        loc.append((x[2],x[3]))
    loc.append(road_map[0][2],road_map[0][3])
    for i in (0,len(loc)-1):
        dist=dist+(sqrt((loc[i][0]-loc[i+1][0])**2 + (loc[i][1]-loc[i+1][1])**2))
    # distance calc sqrt((x1-x2)^2 + (y1-y2)^2)
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    return float(dist)


def swap_cities(road_map, index1, index2):
    new_road_map=copy.deepcopy(road_map)
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
    shiftmap=copy.deepcopy(road_map)
    for i in range(0,len(road_map)):
        if i=0:
            shiftmap[i]=road_map[len(road_map)]
        else:
            shiftmap[i]=road_map[i-1]
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    return shiftmap

def find_best_cycle(road_map):
    count=0
    bestmap=[]
    newmap=[]
    m=0
    best=1000
    while count<10000
        number = random.randint(1,2)
        if number==1:
            newmap=swap_cities(road_map,random.randint(0,len(road_map)),random.randint(0,len(road_map)))
        else:
            newmap=shift_cities(road_map)
        count=count+1
        m=compute_total_distance(newmap)
        if m<=best:
            best=m
            bestmap=newmap
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    return bestmap


def print_map(road_map):
    for x in road_map:
        loc.append((x[2],x[3]))
    loc.append(road_map[0][2],road_map[0][3])
    for i in (0,len(loc)-1):
            dist=(sqrt((loc[i][0]-loc[i+1][0])**2 + (loc[i][1]-loc[i+1][1])**2))
            print('Distance of '+road_map[i][0]+', '+road_map[i][1]+' -> '+road_map[i+1][0]+', '+road_map[i+1][1]+': '+str(float(dist)))
    print('Total Distance for Road_Map: '+str(compute_total_distance(road_map)))

    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """ #cost for each connection is distance of each connection and tot cost is tot distance


def visualise(road_map):
    """
    Need to figure out a way to visualise the road_map!!!!!!!!!!!!!!
    """
    coord=[]
    for x in road_map:
        coord.append((x[2],x[3]))
    maxx=-180
    minx=180
    maxy=-180
    miny=180
    for x in road_map:
        if x[2]>maxx:
            maxx=int(x[2])
        if x[2]<minx:
            minx=int(x[2])
        if x[3]>maxy:
            maxy=int(x[3])
        if x[3]<miny:
            miny=int(x[3])
    #boundaries for the grid are minx, maxx, miny and maxy
    

def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    filename=input("Please input the file name: ")

    read_cities(filename)
    return print_cities(road_map)
    m=find_best_cycle(road_map)
    return m
    return visualise(m)

if __name__ == "__main__": #keep this in
    main()
