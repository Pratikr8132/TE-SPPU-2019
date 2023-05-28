arr=[]
n=int(input("Enter No. of Elemets in the array::::"))
for i in range(n):
    k=int(input("Enter the numbers::::"))
    arr.append(k)

for i in range(n):#step
    min=i
    for j in range(i,n):
        if arr[j]<arr[min]:
            min=j  
    arr[min],arr[i]=arr[i],arr[min] #a,b=b,a
print(arr)


















#
#
#
#
#
#
#
#
#
# Here's an explanation of the code line by line:
#
# arr = []: Initializes an empty list to store the numbers.
#
# n = int(input("Enter No. of Elements in the array::::")): Takes input from the user to determine the number of elements in the array.
#
# for i in range(n):: Iterates n times to input n numbers from the user.
#
# k = int(input("Enter the numbers::::")): Takes input from the user for each number in the array.
#
# arr.append(k): Appends the input number to the arr list.
#
# Outer loop: for i in range(n) represents the step in the selection sort algorithm. It iterates over the indices of the array from 0 to n-1.
#
# min = i: Initializes the min variable as the current index i.
#
# Inner loop: for j in range(i, n) finds the minimum element from the unsorted part of the array.
#
# if arr[j] < arr[min]:: Compares the value at index j with the minimum value found so far.
#
# min = j: If the value at index j is smaller, updates the index of the minimum value.
#
# arr[min], arr[i] = arr[i], arr[min]: Swaps the minimum value with the value at the current index i, placing the minimum value in its correct sorted position.
#
# After the outer loop completes, the array arr is sorted in ascending order.
#
# print(arr): Prints the sorted array.
#
# The time complexity of the selection sort algorithm is O(n^2), where n is the number of elements in the array. The space complexity is O(1) since the sorting is done in-place.
#
# As for the difference between greedy search algorithms and other types of search algorithms, here's a brief comparison:
#
# Greedy search algorithms make locally optimal choices at each step in the hope of finding a global optimum. They focus on immediate gains without considering the long-term consequences.
# Other search algorithms, such as depth-first search, breadth-first search, and A* search, explore the search space systematically and may consider multiple options before making a decision.
# Greedy search algorithms are usually simpler and faster to execute but may not always find the optimal solution. They can get stuck in local optima.
# Other search algorithms provide more comprehensive exploration of the search space and are capable of finding optimal solutions, but they may be slower and require more memory.
# The choice of the s
# earch algorithm depends on the problem at hand, the characteristics of the search space, and the desired trade-offs between solution optimality and computational efficiency.

#
# Certainly! Here's more information about the sorting techniques mentioned:
#
# Bubble Sort:
#
# Bubble Sort works by repeatedly swapping adjacent elements if they are in the wrong order. In each iteration, the largest (or smallest) element "bubbles" up to its correct position.
# It is simple to understand and implement but not efficient for large data sets.
# Bubble Sort has a time complexity of O(n^2) in the average and worst case scenarios, as it needs to compare and swap elements multiple times.
# It is an in-place sorting algorithm, meaning it operates directly on the input array without requiring additional space.
# Selection Sort:
#
# Selection Sort divides the array into two parts: the sorted part and the unsorted part. It repeatedly selects the minimum (or maximum) element from the unsorted part and places it at the beginning of the sorted part.
# Although it performs fewer swaps than Bubble Sort, it still has a time complexity of O(n^2) in all cases.
# Selection Sort is also an in-place sorting algorithm, as it sorts the array by swapping elements within the original array.
# Insertion Sort:
#
# Insertion Sort builds the final sorted array by iteratively inserting each element into its proper position within the sorted part of the array.
# It has a best-case time complexity of O(n) when the input array is already sorted. However, in the average and worst cases, it has a time complexity of O(n^2).
# Insertion Sort is an in-place sorting algorithm and is considered efficient for small data sets or partially sorted arrays.
# Merge Sort:
#
# Merge Sort follows the divide-and-conquer approach. It recursively divides the array into two halves, sorts them independently, and then merges them back together to obtain the sorted array.
# It has a stable sorting property, which means that elements with equal values maintain their relative order after sorting.
# Merge Sort has a time complexity of O(n log n) in all cases. It requires additional space proportional to the size of the input array for merging the subarrays.
# Quick Sort:
#
# Quick Sort also uses the divide-and-conquer technique. It selects a pivot element and partitions the array around the pivot, placing elements smaller than the pivot to its left and larger elements to its right.
# It has good average-case performance and is widely used in practice. However, in the worst case, when the pivot is consistently poorly chosen, it can have a time complexity of O(n^2).
# Quick Sort is an in-place sorting algorithm that requires O(log n) stack space for recursion.
# Heap Sort:
#
# Heap Sort uses a binary heap data structure to sort elements. It first builds a max-heap (or min-heap) from the array and then repeatedly extracts the maximum (or minimum) element to form the sorted array.
# # Heap Sort has a time complexity of O(n log n) in all cases. It is an in-place sorting algorithm but requires additional space for heap construction.
# # These sorting techniques differ in their efficiency, time complexity, space complexity, stability, and suitability for different types and sizes of data sets. The choice of which sorting algorithm to use depends on the specific requirements and characteristics of the data being sorted.
#
#
# tell me which one is better and which one is not
# ChatGPT
# The choice of the "better" sorting algorithm depends on various factors such as the size of the input data, the degree of pre-sorting, memory constraints, and the desired time complexity. Here's a comparison of the sorting techniques mentioned:
#
# Best time complexity for a general case: Merge Sort and Heap Sort have the best time complexity of O(n log n) in all cases. They are efficient for large data sets and guarantee good performance regardless of the input distribution.
#
# Best time complexity for a nearly sorted or small array: Insertion Sort performs well when the input array is already partially sorted or has a small size. It has a best-case time complexity of O(n) and is simple to implement.
#
# Best time complexity for the average case: Quick Sort has an average-case time complexity of O(n log n) and is often faster than Merge Sort and Heap Sort due to its efficient partitioning. However, Quick Sort's worst-case time complexity is O(n^2) if the pivot selection is not optimized.
#
# Stability: Merge Sort is a stable sorting algorithm, meaning it preserves the relative order of elements with equal values. Selection Sort, Quick Sort, and Heap Sort are not inherently stable but can be modified to maintain stability.
#
# Space complexity: Bubble Sort, Selection Sort, and Insertion Sort are in-place sorting algorithms, requiring minimal additional space. Merge Sort and Heap Sort require additional space for merging or heap construction, respectively.
#
# Considering these factors, it's challenging to declare one sorting algorithm as universally better than others. The choice depends on the specific requirements of the sorting task. For example:
#
# If stability is crucial, Merge Sort is preferred.
# For small or nearly sorted arrays, Insertion Sort can be efficient.
# Quick Sort is often used when average-case performance is more important, but it may require careful pivot selection to avoid worst-case behavior.
# Heap Sort is useful when an in-place sorting algorithm is needed with a guaranteed time complexity of O(n log n).
# It's important to analyze the characteristics of the input data and consider the trade-offs between time complexity, space complexity, stability, and other requirements to determine the most suitable sorting algorithm for a particular scenario.