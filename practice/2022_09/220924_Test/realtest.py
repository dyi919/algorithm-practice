def back(e_idx, num_emoticons, prices, answer, users, emoticons):
    if e_idx == num_emoticons:
        num_e_plus_user = 0
        max_total_price = 0

        for rate, min_price in users:
            total_price = 0
            for i in range(num_emoticons):
                if prices[i] >= rate:
                    total_price += emoticons[i] * (100 - prices[i])/100
            if total_price >= min_price:
                num_e_plus_user += 1
            else:
                max_total_price += total_price
        
        if answer[0] < num_e_plus_user:
            answer = [num_e_plus_user, max_total_price]
        elif answer[0] == num_e_plus_user:
            answer = [answer[0], max(answer[1], max_total_price)]
        return

    for i in range(10, 41, 10):
        prices[e_idx] = i
        back(e_idx+1, num_emoticons, prices, answer, users, emoticons)

def solution(users, emoticons):
    answer = [0, 0]
    num_emoticons = len(emoticons)
    prices = [0] * num_emoticons
            
    back(0, num_emoticons, prices, answer, users, emoticons)

    return answer

solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])