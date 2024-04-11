# Sorting

Imagine you're sorting a group of players by height.
How might you do that?

## Bubble Sort

Start from the left and move right comparing two players at a time. If the left player is taller than the right player than swap them.
Repeat this process until you reach the end. If you reach the end and you made any swaps than start from the beginning again.
Repeat until you go from left to right without making any swaps.

- Start at index 0 of list.
- If left is larger than right swap them and flag as unsorted

```python
nums = [20, 13, 3, 3, 4, 5, 1, 2, 8, 7, 9, 0, 11]

def bubble_sort(nums):
  sorted = False

  while not sorted:
    sorted = True
    for i in range(0, len(nums) - 1):
      if nums[i] > nums[i + 1]:
        sorted = False
        nums[i], nums[i + 1] = nums[i + 1], nums[i]

  return nums
print('Bubble Sort:', bubble_sort(nums))
```

## Selection Sort

Start from the left end of the lineup and move right. While moving right track the position of the shortest player in the list with a marker.
Once you reach the end, if the shortest player isn't on the far left then swap them with the farthest left position.

- Loop from idx `0` of list.
  - Set `arr[i]` as `min`.
  - Loop from idx `i+1` of list, aka `j`.
    - If any `arr[j]` < `arr[min]`
      - Set `min` to be `j`.
  - If `min != i`
    - Swap arr[min]

```python
nums = [20, 13, 3, 3, 4, 5, 1, 2, 8, 7, 9, 0, 11]

def selection_sort(nums):
    for i in range(len(nums)):
        min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min]:
                min = j
        if min != i:
            nums[min], nums[i] = nums[i], nums[min]

    return nums
print('Selection Sort:', selection_sort(nums))
```

## Insertion Sort

```python
nums = [20, 13, 3, 3, 4, 5, 1, 2, 8, 7, 9, 0, 11]

def insertion_sort(nums):
	for i in range(1, len(nums)):
		val = nums[i]
		while nums[i-1] > val and i > 0:
			nums[i], nums[i-1] = nums[i-1], nums[i]
			i -= 1
	return nums

print(insertion_sort(nums))
```

## Merge Sort

```python
#
nums = [20, 13, 3, 3, 4, 5, 1, 2, 8, 7, 9, 0, 11]
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    midIdx = len(arr) // 2
    print(midIdx)
    l = arr[:midIdx]
    r = arr[midIdx:]
    return merge(merge_sort(l), merge_sort(r))


def merge(left, right):
    res = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1

    res.extend(left[l:])
    res.extend(right[r:])

    return res
print(merge_sort(nums))
```
