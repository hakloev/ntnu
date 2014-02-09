from sys import stdin

def sorter(A):
    # Merk: den sorterte lista ma returneres
    # SKRIV DIN KODE HER
    # Insertion-sort
     for index in xrange(1, len(A)):
         curr = A[index]
         prev = index - 1
         while prev >= 0 and A[prev] > curr:
             A[prev + 1] = A[prev]
             prev = prev -1
         A[prev + 1] = curr
     return A

   # Insertion-sort when short list, quick-sort else
   # l = len(A)
   # if l < 6:
   #     return insertionSort(A)
   # else:
   #     less = []
   #     equal= []
   #     greater = []
   #     pivot = A[0]
   #     for num in A:
   #         if num < pivot:
   #             less.append(num)
   #         elif num == pivot:
   #             equal.append(num)
   #         else:
   #             greater.append(num)
   #     return sorter(less) + sorter(equal) + sorter(greater) 
    
#def insertionSort(A):
#    for index in xrange(1, len(A)):
#        curr = index
#        while A[curr] < A[curr - 1] and curr > 0:
#            temp = A[curr]
#            A[curr] = A[curr-1]
#            A[curr - 1] = temp
#            curr -= 1
#    return A

# Binary search
def binary(A, target):
    low = 0
    high = (len(A) - 1)
    while low <= high:
        mid = ((low + high) // 2)
        if target == A[mid]:
            break
        elif target < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return mid

def finn(A, nedre, ovre):
    # Merk: resultatet ma returneres
    # SKRIV DIN KODE HER
    min_index = binary(A, nedre)
    max_index = binary(A, ovre)
    if A[min_index] > nedre and min_index != 0:
        min_index -= 1
    if A[max_index] < ovre and max_index != len(A) - 1:
        max_index += 1
    return [A[min_index], A[max_index]]

if __name__ == "__main__":
    liste = [int(x) for x in stdin.readline().split()]

    sortert = sorter(liste)
    #print(sortert)

    for linje in stdin:
        ord = linje.split()
        minst = int(ord[0])
        maks = int(ord[1])
        resultat = finn(sortert, minst, maks)
        print str(resultat[0]) + " " + str(resultat[1])