def solution(fees, records):
    num_records = len(records)
    records_list = []
    car_list = {}
    
    for i in range(num_records):
        records_list.append(records[i].split()+[0]+[0])
        car_list[records_list[i][1]] = [0, 0]  
    records_list.sort(key=lambda x: x[1])
    
    for i in range(num_records):
        total_time = 0
        if records_list[i][2] == 'IN':
            if i < num_records-1 and records_list[i][1] == records_list[i+1][1]:
                total_time = (int(records_list[i+1][0][:2]) - int(records_list[i][0][:2])) * 60 + int(records_list[i+1][0][3:]) - int(records_list[i][0][3:])
                car_list[records_list[i][1]][0] += total_time
            else:
                total_time = (23 - int(records_list[i][0][:2])) * 60 + 59 - int(records_list[i][0][3:])
                car_list[records_list[i][1]][0] += total_time     
    
    for v in car_list.values():
        v[1] = calc_fee(fees, v[0])
    
    ans = sorted(list(car_list.items()))
    return [x[1][1] for x in ans]

def calc_fee(fees, time):
    base_time, base_fee, unit_time, unit_fee = fees
    if time <= base_time:
        return base_fee
    else:
        total_fee = base_fee
        time -= base_time
        total_fee += unit_fee * (time // unit_time)
        total_fee += unit_fee if time % unit_time > 0 else 0
        return total_fee