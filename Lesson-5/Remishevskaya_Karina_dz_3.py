tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

from itertools import zip_longest

tutor_gen = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses) if tutor is not None)

n = 0

while n < len(tutors):
    n += 1
    print(next(tutor_gen))

# def tutor_gen(x, y):
#     if len(tutors) >= len(klasses):
#         gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
#     else:
#         gen = ((tutor, None) for tutor, klass in zip(tutors, klasses))
#     yield gen
#
#
# print(*tutor_gen())
