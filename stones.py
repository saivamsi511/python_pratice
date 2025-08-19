def get_unique_stones_to_bring(M,N,common_stones):
    mars_weight = list(range(1,M+1))
    earth_weights = common_stones
    mars_set = set(mars_weight)
    earth_set = set(earth_weights)
    unique_mars_weights = list(mars_set -earth_set)
    unique_mars_weights.sort()
    total_weight = 0
    num_stones_selected = 0
    for weights in unique_mars_weights:
        if total_weight + weights <= M:
            total_weight +=weights
            num_stones_selected +=1
        else:
            break
    return num_stones_selected
input1 = int(input("Enter the capacity of rob's bag:-"))
input2 = int(input("Enter no.of common stones on earth:-"))
input3 = list(map(int,input("list of stones from earth:-")))

output = get_unique_stones_to_bring(input1,input2,input3)
print(output)