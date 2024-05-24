#Lab 10
#Amra Ibrahim
#CSMC 254

def get_available_data(plan_allowance, usage_list):
    months_data = plan_allowance
    for x in range(len(usage_list)):
        usage= plan_allowance- usage_list[x]
        months_data= usage + months_data
    return months_data


def final_location(swaps):
    location = 1 
    for move in swaps:
        if move == 'A':
            if location == 1:
                location = 2
            elif location == 2:
                location = 1
        elif move == 'B':
            if location == 3:
                location = 2
            elif location == 2:
                location = 3
        elif move == 'C':
            if location == 1:
                location = 3
            elif location == 3:
                location = 1
            else: return 'Error' 
    return location


if __name__ == "__main__":
    # test with no excess expect output to be plan_allowance
    print (str(get_available_data(5, [5, 4, 5, 5, 3])))
    print (str(final_location ('ABCAABCCBA')))