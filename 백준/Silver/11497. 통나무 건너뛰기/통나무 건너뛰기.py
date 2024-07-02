from collections import deque
for _ in range(int(input())):
  N = input()
  heights = deque(sorted(map(int, input().split())))

  max_grade = 0

  cur_left = heights[0]
  cur_right = heights[0]
  
  heights.popleft()
  while heights:
    if len(heights) != 1:
      height1 = heights.popleft()
      height2 = heights.popleft()
      if max(abs(cur_left-height1),abs(cur_right-height2)) < max(abs(cur_left-height2),abs(cur_right-height1)):
        max_grade = max(max_grade, abs(cur_left-height1), abs(cur_right-height2))
        cur_left = height1
        cur_right = height2
      else:
        max_grade = max(max_grade, abs(cur_left-height2), abs(cur_right-height1))
        cur_left = height2
        cur_right = height1
    else:
      height = heights.popleft()
      max_grade = max(max_grade, abs(cur_left-height), abs(cur_right-height))
  
  print(max_grade)