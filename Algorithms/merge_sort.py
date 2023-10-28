A = [7, 5, 3, 8, 2, 4, 9, 1]



# Better readable code
def merge(A, B):
    C = []
    i = j = k = 0

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    
    if i < len(A):
        while(i < len(A)):
            C.append(A[i])
            i += 1
    else:
        while(j < len(B)):
            C.append(B[j])
            j += 1
    return C


def mergesort_new(A):
     
    if len(A) > 1:

        mid = len(A)//2   
        left = A[:mid]
        right = A[mid:]

        merged_left = mergesort_new(left)
        merged_right = mergesort_new(right)
        res = merge(merged_left, merged_right)

        return res

    else:
        return A
    
res = mergesort_new(A)
print(A, res)


def mergesort(A):
    if len(A) > 1:
        mid = len(A) // 2

        L = A[:mid]
        R = A[mid:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1


