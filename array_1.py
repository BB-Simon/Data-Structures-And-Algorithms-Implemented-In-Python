def search(arr, n, key):
  for i in range(n):
    if(arr[i] == key):
      return i
  
  return -1


arr = [2, 3, 4, 65, 67, 12]
n = len(arr)
key = 65
idx = search(arr, n, key)

# if(idx != -1):
#   print('Element fount at position: ' + str(idx + 1))
# else:
#   print('Element not found')

