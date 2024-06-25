def min_dice_rolls(A):
    target = A - 1
    max_roll = 6
    rolls = target // max_roll
    if target % max_roll != 0:
        rolls += 1
    return rolls

if __name__ == "__main__":
    A = int(input().strip())
    print(min_dice_rolls(A))
