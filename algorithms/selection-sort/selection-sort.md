## Selection Sort

To sort a list in an order (say descending order ), you can search for the highest item in the list and put that as the first element of a new list. Then you find the next highest and move it as the second highest item in the new list, and so on until you have a full sorted list. 
This is what selection sort does. It has an O(n^2) time complexity because for each item that will be placed in the sorted list, you'd have to look through the original list again.