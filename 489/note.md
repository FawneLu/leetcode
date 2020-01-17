### 扫地机器人
我们需要确定的是机器人的起始位置是（0，0），且初始方向是往上走。  
扫地机器人后退：先旋转180度，往前走一步，再旋转180度。
```python
def goback(robot):
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnRight()
            robot.turnRight()
```