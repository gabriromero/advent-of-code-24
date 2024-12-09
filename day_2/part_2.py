
from typing import List


def retrieve_reports_from_input() -> List[List[int]]:
    reports: List[List[int]] = []

    with open('day_2/data/input.txt') as file:
        for line in file.readlines():
            report = list(map(int, line.split()))
            reports.append(report)

    return reports

def levels_are_safe(level_1: int, level_2: int, is_increasing: bool) -> bool:
    return ((abs(level_1 - level_2) <= 3) and 
            ((is_increasing and level_2 > level_1) or 
             (not is_increasing and level_2 < level_1)))

def get_safe_reports_count(reports: List[List[int]]):
    safe_reports_count = 0
    for report in reports:
        found_safe_report = False
        for j in range(len(report)):
            is_increasing = False
            partial_report = [x for i, x in enumerate(report) if i != j]
            for i in range(len(partial_report)-1):
                if i == 0 and partial_report[0] < partial_report[1]:
                    is_increasing = True

                if not levels_are_safe(partial_report[i], partial_report[i+1], is_increasing):
                    break

                if i == len(partial_report) - 2:
                    safe_reports_count += 1
                    found_safe_report = True
            
            if found_safe_report:
                break

    return safe_reports_count

def main():
    reports = retrieve_reports_from_input()

    safe_reports_count = get_safe_reports_count(reports)

    print(safe_reports_count)


if __name__ == '__main__':
    main()