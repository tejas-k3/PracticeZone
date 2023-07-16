# https://leetcode.ca/2016-08-09-253-Meeting-Rooms-II/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0
        # The heap initialization
        freeRooms = []
        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])
        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(freeRooms, intervals[0][1])
        # For all the remaining meeting rooms
        for i in intervals[1:]:
            # If the room due to free up the earliest is free, assign that room to this meeting.
            if freeRooms[0] <= i[0]:
                heapq.heappop(freeRooms)
            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(freeRooms, i[1])
        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(freeRooms)