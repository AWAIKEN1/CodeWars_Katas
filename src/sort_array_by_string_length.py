def sort_by_length(arr):
    return sorted(arr, key=len)




#   n = len(arr)

#   for i in range(n):
#       for j in range(0, n - i - 1):
#           if len(arr[j]) > len(arr[j + 1]):
#               arr[j], arr[j + 1] = arr[j + 1], arr[j]

#   return arr