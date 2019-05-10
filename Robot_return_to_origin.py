class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        from collections import Counter

        c = Counter(list(moves))

        Left = c['L']
        Right = c['R']
        Down = c['D']
        Up = c['U']

        if Right - Left == 0 and Up - Down == 0:
            return True
        else:
            return False

# '''Option 2: Little slower, but still works!'''
# '''Count individually, then calculate'''
# Left = list(moves).count('L')
# Right = list(moves).count('R')
# Down = list(moves).count('D')
# Up = list(moves).count('U')
#
# if Right - Left == 0 and Up - Down == 0:
#     return True
# else:
#     return False


# '''Option 3: Slow, but works!'''
# '''Go through moves, indivudually, then see if at (0,0)
# UpDown = 0
# LeftRight = 0
#
# for move in moves:
#     if move == 'U':
#         UpDown += 1
#     if move == 'D':
#         UpDown -= 1
#     if move == 'R':
#         LeftRight += 1
#     if move == 'L':
#         LeftRight -= 1
#
# if UpDown == 0 and LeftRight == 0:
#     return True
# else:
#     return False
