class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0:
                    top_asteroid = stack.pop()
                    if top_asteroid == -asteroid:
                        break
                    elif top_asteroid > -asteroid:
                        stack.append(top_asteroid)
                        break
                    else:
                       
                        pass
                else:
                    stack.append(asteroid)

        return stack
