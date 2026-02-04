def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
    arr.sort()
    answer = []
    min_diff = float('inf')

    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        if min_diff > diff:
            min_diff = diff
    
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        if min_diff == diff:
            answer.append([arr[i],arr[i+1]])

    return answer        