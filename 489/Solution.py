```python
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        def goback(robot):
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def dfs(pos,robot,d,visited):
            if pos in visited:
                return
            visited.add(pos)
            
            robot.clean()
            
            for i in directions:
                if robot.move():
                    dfs((pos[0]+directions[d][0],pos[1]+directions[d][1]),robot,d,visited)
                    goback(robot)
                robot.turnRight()
                d=(d+1)%(len(directions))
        
        dfs((0,0),robot,0,set())
```