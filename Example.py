import random

try:
    import matplotlib.pyplot as plt

    def draw_random_circles(n):
        if n <= 0:
            raise ValueError("Number of circles must be positive")

        fig, ax = plt.subplots()
        for _ in range(n):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            radius = random.uniform(0.01, 0.1)
            color = (random.random(), random.random(), random.random())
            circle = plt.Circle((x, y), radius, color=color, alpha=0.6)
            ax.add_patch(circle)

        ax.set_aspect('equal')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        plt.title(f"{n} Random Circles")
        plt.show()

    # Try changing this to 0 or a string to see exception handling in action
    draw_random_circles(10)

except ImportError:
    print("matplotlib is not installed! Try: pip install matplotlib")
except ValueError as ve:
    print("Value error:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)
