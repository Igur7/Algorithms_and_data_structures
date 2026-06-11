import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
def orientation(p,q,r):
    sigma = (q.y - p.y) * (r.x  - q.x)
    tau = (q.x - p.x) * (r.y - q.y)

    value = sigma - tau

    if value == 0:
        return 0
    elif value > 0:
        return 1 # ze wskazówkami
    else:
        return 2 # przeciwnie do wskazówek

def distance_squared(p1, p2):
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2

def leftmost_point(points):
    leftmost = points[0]
    for point in points:
        if point.x < leftmost.x or (point.x == leftmost.x and point.y < leftmost.y):
            leftmost = point
    return leftmost

def next_point(points, p):
    index = points.index(p)
    return points[(index + 1) % len(points)]

def jarvis_basic(points):
    if len(points) <= 2:
        return points
    
    start = leftmost_point(points)
    ans = []
    p = start

    while True:
        ans.append(p)
        q = next_point(points, p)

        for r in points:
            if r == p:
                continue
            o = orientation(p, q, r)

            if o == 1:
                q = r
            elif o == 0:
                continue
        p = q

        if p == start:
            break
    return ans

def jarvis(points):
    if len(points) <= 2:
        return points
    
    start = leftmost_point(points)
    ans = []
    p = start

    while True:
        ans.append(p)
        q = next_point(points, p)

        for r in points:
            if r == p:
                continue
            o = orientation(p, q, r)

            if o == 1:
                q = r
            elif o == 0:
                if distance_squared(p, r) > distance_squared(p, q):
                    q = r
        p = q

        if p == start:
            break
    return ans

def lowest_point(points):
    best = points[0]
    for p in points:
        if p.y < best.y or (p.y == best.y and p.x < best.x):
            best = p
    return best


def sort_by_angle(points, p0):
    sorted_points = points[:]

    for i in range(1, len(sorted_points)):
        current = sorted_points[i]
        j = i - 1

        while j >= 0 and is_before(current, sorted_points[j], p0):
            sorted_points[j + 1] = sorted_points[j]
            j -= 1

        sorted_points[j + 1] = current

    return sorted_points

def is_before(p1, p2, p0):
    o = orientation(p0, p1, p2)

    if o == 0:
        return distance_squared(p0, p1) < distance_squared(p0, p2)

    return o == 2

def graham(points):
    if len(points) <= 2:
        return points
    
    p0 = lowest_point(points)

    others = [p for p in points if p != p0]
    sorted_points = sort_by_angle(others, p0)

    no_duplicates = []

    i = 0
    while i < len(sorted_points):
        while i < len(sorted_points) - 1 and orientation(p0, sorted_points[i], sorted_points[i + 1]) == 0:
            i += 1
        no_duplicates.append(sorted_points[i])
        i += 1

    if len(no_duplicates) < 2:
        return []

    stack = [p0, no_duplicates[0], no_duplicates[1]]

    for p in no_duplicates[2:]:
        while len(stack) > 1 and orientation(stack[-2], stack[-1], p) != 2:
            stack.pop()
        stack.append(p)
    return stack

def plot_hulls(results):
    rows = (len(results) + 1) // 2
    fig, axes = plt.subplots(rows, 2, figsize=(12, 4 * rows))

    if hasattr(axes, "flatten"):
        axes = axes.flatten()
    else:
        axes = [axes]

    for ax, (title, points, hull) in zip(axes, results):
        ax.scatter([p.x for p in points], [p.y for p in points], color="black", zorder=2)

        for point in points:
            ax.text(point.x + 0.05, point.y + 0.05, str(point), fontsize=8)

        if hull:
            closed_hull = hull + [hull[0]]
            ax.plot(
                [p.x for p in closed_hull],
                [p.y for p in closed_hull],
                color="red",
                linewidth=2,
                marker="o",
                zorder=3
            )

        ax.set_title(title)
        ax.set_aspect("equal", adjustable="box")
        ax.grid(True)

    for ax in axes[len(results):]:
        ax.axis("off")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    points1 = [Point(0, 3), Point(0, 0), Point(0, 1), Point(3, 0), Point(3, 3)]
    points2 = [Point(0, 3), Point(0, 1), Point(0, 0), Point(3, 0), Point(3, 3)]
    points3 = [Point(2, 2), Point(4, 3), Point(5, 4), Point(0, 3), Point(0, 2), Point(0, 0), Point(2, 1), Point(2, 0), Point(4, 0)]
    points4 = [Point(0, 3), Point(1, 1), Point(2, 2), Point(4, 4), Point(0, 0), Point(1, 2), Point(3, 1), Point(3, 3)]

    jarvis_basic_1 = jarvis_basic(points1)
    jarvis_basic_2 = jarvis_basic(points2)
    jarvis_fixed_1 = jarvis(points1)
    jarvis_fixed_2 = jarvis(points2)
    jarvis_basic_3 = jarvis_basic(points3)
    jarvis_fixed_3 = jarvis(points3)
    graham_result = graham(points4)

    print("Jarvis basic 1:", jarvis_basic_1)
    print("Jarvis basic 2:", jarvis_basic_2)
    print("Jarvis fixed 1:", jarvis_fixed_1)
    print("Jarvis fixed 2:", jarvis_fixed_2)
    print("Jarvis basic 3:", jarvis_basic_3)
    print("Jarvis fixed 3:", jarvis_fixed_3)
    print("Graham:", graham_result)

    plot_hulls([
        ("Jarvis basic 1", points1, jarvis_basic_1),
        ("Jarvis basic 2", points2, jarvis_basic_2),
        ("Jarvis fixed 1", points1, jarvis_fixed_1),
        ("Jarvis fixed 2", points2, jarvis_fixed_2),
        ("Jarvis basic 3", points3, jarvis_basic_3),
        ("Jarvis fixed 3", points3, jarvis_fixed_3),
        ("Graham", points4, graham_result)
    ])
