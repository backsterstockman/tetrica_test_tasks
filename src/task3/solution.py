def pairify(times: list[dict]) -> list[tuple[int, int]]:
    return list(zip(times[0::2], times[1::2]))


def merge(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not intervals:
        return []

    ints = sorted(intervals, key=lambda x: x[0])
    merged = [ints[0]]
    for s, e in ints[1:]:
        last_s, last_e = merged[-1]
        if s <= last_e:
            merged[-1] = (last_s, max(e, last_e))
        else:
            merged.append((s, e)) 
    return merged


def intersect(
        first_intervals: list[tuple[int, int]],
        second_intervals: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    res = []
    for s1, e1 in first_intervals:
        for s2, e2 in second_intervals:
            start = max(s1, s2)
            end = min(e1, e2)
            if start < end:
                res.append((start, end))
    return res


def time_together(intervals: dict[str, list[int]]) -> int:
    lesson = pairify(intervals['lesson'])
    pupil = merge(pairify(intervals['pupil']))
    tutor = merge(pairify(intervals['tutor']))

    lp = intersect(lesson, pupil)
    lpt = intersect(lp, tutor)

    return sum(end - start for start, end in lpt)


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = time_together(test['intervals'])
       print(test_answer)
    #    assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
