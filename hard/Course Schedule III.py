def scheduleCourse(courses) -> int:
    courses = sorted(courses, key=lambda course: course[1])
    total_courses = 0
    for i in range(len(courses)):
        cur_total_courses = 0
        cur_sum = 0
        for j in range(i, len(courses)):
            duration, last_day = courses[j]
            if cur_sum + duration > last_day:
                continue
            cur_sum += duration
            cur_total_courses += 1
        total_courses = max(total_courses, cur_total_courses)

    return total_courses


def scheduleCourse2(courses) -> int:
    courses.sort()
    print(courses)
    total_courses = 0
    max_duration = 0
    for i in range(len(courses)):
        cur_total_courses = 0
        cur_sum = 0
        for j in range(i, len(courses)):
            duration, last_day = courses[j]

            if cur_sum + duration > last_day:

                if cur_sum - max_duration + duration < last_day:
                    cur_sum -= max_duration
                    cur_total_courses -= 1
                else:
                    continue
            cur_sum += duration
            cur_total_courses += 1
            max_duration = duration
        total_courses = max(total_courses, cur_total_courses)

    return total_courses

print(scheduleCourse2([[860, 4825], [13, 1389], [746, 8823], [455, 2778], [233, 2069], [106, 5648], [802, 2969], [958, 2636], [567, 2439],
     [623, 1360], [700, 4206], [9, 3725], [241, 7381]]))

# assert scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]) == 3
# assert scheduleCourse([[1, 2]]) == 1
# assert scheduleCourse([[3, 2], [4, 3]]) == 0
# assert scheduleCourse([[5, 5], [4, 6], [2, 6]]) == 2
# assert scheduleCourse(
#     [[860, 4825], [13, 1389], [746, 8823], [455, 2778], [233, 2069], [106, 5648], [802, 2969], [958, 2636], [567, 2439],
#      [623, 1360], [700, 4206], [9, 3725], [241, 7381]]) == 12
# assert scheduleCourse([[5, 6], [3,7], [4,7], [5,12], [1,12], [1,12], [2,12]]) == 5