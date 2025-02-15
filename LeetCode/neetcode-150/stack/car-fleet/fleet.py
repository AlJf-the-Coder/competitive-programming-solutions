from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        slowest = -1
        for p, s in cars:
            time = (target - p) / s
            if time > slowest:
                slowest = time
                fleets += 1
        return fleets

class Solution1:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = []
        fleet = [cars[0]]
        slowest = cars[0]
        for car in cars[1:]:
            p1, v1 = slowest
            p2, v2 = car
            if v1 != v2 and p1 <= p1 + v1 * ((p1 - p2)/(v2 - v1)) <= target:
                fleet.append(car)
            else:
                slowest = car
                fleets.append(fleet)
                fleet = [slowest]
        fleets.append(fleet)
        return len(fleets)

