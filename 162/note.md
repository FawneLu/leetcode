### 可以用二分的思路求解
We start off by finding the middle element, midmid from the given numsnums array. 
If this element happens to be lying in a descending sequence of numbers. 
or a local falling slope(found by comparing nums[i]nums[i] to its right neighbour), 
it means that the peak will always lie towards the left of this element. 
Thus, we reduce the search space to the left of midmid(including itself) and perform the same process on left subarray.

If the middle element, midmid lies in an ascending sequence of numbers, 
or a rising slope(found by comparing nums[i]nums[i] to its right neighbour), 
it obviously implies that the peak lies towards the right of this element. 
Thus, we reduce the search space to the right of midmid and perform the same process on the right subarray.

In this way, we keep on reducing the search space till we eventually reach a state where only one element is remaining in the search space. 
This single element is the peak element.