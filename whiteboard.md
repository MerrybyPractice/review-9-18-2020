# Q: Given a set of non-overlaping intervals insert a new interval into the intervals, merge if necessary. You may assume that the intervals were initally sorted according to the start tiems. 

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

- interval == sub list
- stored in a list
- if an interval would overlap, instead extend the exsiting interval to contain those numbers. 
- Intervals will always be positive 
- Intervals will always be whole numbers
- Input intervals list could be empty, one, or many
- Only ever adding one at a time 

1. in = [], [x,x] empty intervals [X]
2. in = [[x,x]], [x,x] intervals of one
3. in = [[x,x], [x,x,]], [x,x] intervals of 2
4. in = [[x,x], [x,x], [x,x], [x,x]], [x,x] intervals of many
5. in = [[1,2]], [1,2] equal
6. in = [[2,3]], [0,1] interval les than 
7. in = [[2,3]], [1,2] interval less than but would merge
8. in = [[1,2]], [3,4] interval greater than 
9. in = [[1,2]], [2,3] interval greater than but would merge

insert: 
    intervals = [[]]
    newInterval = []
iterate over the intrvals list 
    - I want to check the begining and end of each interval again the newInterval. 
      - beging - beginingNew: 
        - newInterval less than: 
          - begining-endNew 
            - newInterval less than:
              - insert before 
            - newInterval greater than:  
              - merge. 
        - newInterval greater than:  
          - end-beginingNew
            - newInterval less than: 
              - merge
            - newInterval greater than:  
              - insert after
       
    - end - endNEw 
        - newInterval less than: 
          - begining-endNew
            - newInterval less than: 
              - shouldnt ever happen? - covered in begining checks
            - newInterval greater than:  
                - merge
        - newInterval greater than: 
          - insert after
 
merge 
    interval = []
    newInterval = []

        create empty list 
            index[0] == interval[0] 
            index[1] == newInterval[1]
        return empty list 

insert 

Insert_interval - O(n)
merge_intervals - O(logn)
insert_sepcific_position = O(n)

O(2n)