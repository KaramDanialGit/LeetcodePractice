# RESOURCE: https://leetcode.com/discuss/interview-question/390456/Google-or-Phone-Screen-or-Piles-of-Boxes

def level_boxes(boxes):
    boxes.sort(reverse = True)
    steps = 0
    i = 0

    while i < len(boxes) - 1:
        if boxes[i + 1] < boxes[i]:
            steps += i + 1
        i += 1
    return steps

print(level_boxes([150, 150, 210, 80, 110]))