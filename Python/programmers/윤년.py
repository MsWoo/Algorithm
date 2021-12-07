def solution(a, b):
    day = 0
    
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(a-1):
        day += months[i]
        
    day += b-1
    day %= 7
    
    return days[day]