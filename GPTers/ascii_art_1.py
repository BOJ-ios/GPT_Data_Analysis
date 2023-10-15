import os
import time
import math


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_shapes(tick):
    lines = [' ' * 40 for _ in range(20)]
    width, height = 40, 20

    # Draw circle
    for i in range(height):
        for j in range(width):
            d = math.sqrt((j - 20)**2 + (i - 10)**2)
            if 8 < d < 9:
                lines[i] = lines[i][:j] + 'O' + lines[i][j+1:]

    # Draw moving square
    x = int(5 * math.sin(tick / 10.0) + 20)
    y = int(5 * math.cos(tick / 10.0) + 10)
    for i in range(max(y, 0), min(y + 3, height)):
        lines[i] = lines[i][:max(x, 0)] + '#' * 3 + \
            lines[i][min(x + 3, width):]

    # Draw lines
    print('\n'.join(lines))


def animate_shapes():
    tick = 0
    while True:
        clear_screen()
        draw_shapes(tick)
        time.sleep(0.1)
        tick += 1


if __name__ == "__main__":
    animate_shapes()
