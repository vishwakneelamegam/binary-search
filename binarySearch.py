def binarySearch(dataList,searchData):
    try:
       lowerBound = 0
       upperBound = len(dataList) - 1
       while lowerBound <= upperBound:
           mid = (lowerBound + upperBound) // 2
           if(dataList[mid] == searchData):
              return True
           else:
              if dataList[mid] < searchData:
                 lowerBound = mid + 1
              if dataList[mid] > searchData:
                 upperBound = mid - 1
       return False
    except Exception as e:
       return e

listData = ["apple","grape","guava","orang"]

print(binarySearch(listData,"apple"))
