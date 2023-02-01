# https://school.programmers.co.kr/learn/courses/30/lessons/77486

def solution(enroll, referral, seller, amount):
    N = len(enroll)
    S = len(seller)
    
    parent_list = {e: "" for e in enroll}
    revenue_list = {e: 0 for e in enroll}
    
    for i in range(N):
        parent_list[enroll[i]] = referral[i]
            
    def calc_revenue(member, revenue):
        if revenue < 1 or member == '-':
            return

        dividend = revenue // 10
        revenue -= dividend

        revenue_list[member] += revenue
        calc_revenue(parent_list[member], dividend)
        
        return
    
    for i in range(S):
        calc_revenue(seller[i], amount[i] * 100)
    
    return [revenue_list[member] for member in enroll]