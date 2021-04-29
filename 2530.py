hour,minute,second = map(int,input().split()) 
time = int(input())
second = second + time
minute += second // 60
hour += minute // 60
second = second%60 
minute = minute%60
hour = hour%24
print(hour,minute,second)