
def calculate_order_day_to_vendor(input_list):
"""
This method counts the number of days from the day order was sent to the vendor 
"""
    sample = [0,0,1,0,0,0,1]
    index = 0
    day_count = 0
    curr_1_index = -1
    loop_count = 1
    while input_list.count(1) > 0 and loop_count <= (len(input_list) * 2 + 1):
        try:
            if input_list[index] >= 1:
                if curr_1_index < 0:
                    # for the first non zero value, do not update the array
                    curr_1_index = index
                    day_count = 1
                else:
                    # Update the array and reset counters
                    input_list[curr_1_index] = day_count
                    day_count = 1
                    curr_1_index = index
            elif input_list[index] == 0 and curr_1_index >= 0:
                day_count += 1
            index += 1
            loop_count += 1
        except IndexError:
            index = 0
            loop_count += 1

    print(input_list)
    return input_list
