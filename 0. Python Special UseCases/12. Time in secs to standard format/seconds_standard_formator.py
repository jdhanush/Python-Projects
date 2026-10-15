list_1 = [2000]
list_2 = [4500, 7009, 8789, 86400]




def time_formater_list(time_list):
    def time_formater_single_element(x):
        hours = int(x // 3600)
        minutes = int((x % 3600) // 60)
        seconds = int(x % 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
    timestamp_list = []
    for e in range(len(time_list)):
        timestamp = time_formater_single_element(time_list[e])
        timestamp_list.append(timestamp)
    return timestamp_list


print(time_formater_list(list_1))
print(time_formater_list(list_2))
