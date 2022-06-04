# 220604 이동언

from math import ceil

SPRING = [3, 4, 5]
SUMMER = [6, 7, 8]
FALL = [9, 10, 11]
WINTER = [12, 1, 2]

FRUIT_PER_PERSON = {
    "strawberry": 5,
    "watermelon": 0.1,
    "apple": 1,
    "pear": 0.5,
}

KOREAN_NAMES = {
    "strawberry": "딸기",
    "watermelon": "수박",
    "apple": "사과",
    "pear": "배",
}

# returns the season of the given month
# season - 0: spring, 1: summer, 2: fall, 3: winter, -1: error
def get_season(month):
    if month in SPRING:
        return 0
    elif month in SUMMER:
        return 1
    elif month in FALL:
        return 2
    elif month in WINTER:
        return 3
    else:
        return -1

# returns the list of desserts available for the given season
def get_season_desserts_list(season):
    if 0 <= season < 2:
        return ["strawberry", "watermelon"]
    elif 2 <= season < 4:
        return ["apple", "pear"]
    else:
        return []

# returns the index of the dessert provided given the date
def get_daily_dessert(date):
    remainder = date % 10
    if remainder == 1 or remainder == 5:
        return 0
    elif remainder == 3 or remainder == 7:
        return 1
    else:
        return -1

# returns the total number of the desserts to be provided
def get_number_of_dessert(dessert, soldiers):
    return ceil(FRUIT_PER_PERSON[dessert] * float(soldiers))

# print the record for the month
def print_record(month, soldiers):
    print("%d월 디저트 구매내역서 (총 %d명)" % (current_month, total_soldiers))

    current_season = get_season(current_month)
    season_desserts = get_season_desserts_list(current_season)

    for date in range(1, 31):
        dessert_index = get_daily_dessert(date)
        if dessert_index != -1:
            dessert = season_desserts[dessert_index]  
            number_of_dessert = get_number_of_dessert(dessert, soldiers)
            print("%d월 %d일: %s %d개" % (month, date, KOREAN_NAMES[dessert], number_of_dessert))
        else:
            print("%d월 %d일: -" % (month, date))

current_month = 3
total_soldiers = 70

print_record(current_month, total_soldiers)