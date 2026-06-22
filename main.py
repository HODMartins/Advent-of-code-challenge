def safe(report):
    diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)


def is_safe_with_dampener(report):
    if safe(report):
        return True

    for i in range(len(report)):
        reduced = report[:i] + report[i + 1:]
        if safe(reduced):
            return True

    return False


def solve(filename="report_input.txt"):
    with open(filename, "r") as file:
        reports = [list(map(int, line.split())) for line in file if line.strip()]

    part1 = sum(safe(report) for report in reports)
    part2 = sum(is_safe_with_dampener(report) for report in reports)

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == "__main__":
    solve()