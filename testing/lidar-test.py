def plot_points(points, size=9):
    grid = [["." for _ in range(size)] for _ in range(size)]
    center = size // 2

    for p in points:
        x = int(round(p.real)) + center
        print(x)
        y = center - int(round(p.imag))
        print(y)
        if 0 <= x < size and 0 <= y < size:
            grid[y][x] = "#"

    grid[center][center] = "R"  # Rover position

    for row in grid:
        print(" ".join(row))
        
def main():
    print("Hello World")
    # import numpy as np
    
    # Simulated LIDAR point cloud (meters)
    points = [
        -2 + -2j,  3 + 2j,  4 + 1j,
        1 + 3j,  0 + 4j, -1 + 3j,
       -2 + 2j, -3 + 1j, -2 + 0j,
       1 + 1j
    ]
    plot_points(points)

main()
