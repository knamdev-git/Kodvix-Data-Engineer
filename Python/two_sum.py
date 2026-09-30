arr = [2, 7, 11, 15]
target = 9

start = 0
end = len(arr) - 1

pairs =  set()

for curr in arr :
    sum = arr[end] + arr[start]  
    if sum > target:
        end -= 1
    elif sum < target : 
        start += 1
    else :  
        pairs.add((arr[start], arr[end]))
        end -= 1
        start += 1

print(pairs)