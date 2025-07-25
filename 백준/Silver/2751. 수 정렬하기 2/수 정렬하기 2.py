from typing import MutableSequence
import sys


def merge_sort(a: MutableSequence) -> None:

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)
            _merge_sort(a, center + 1, right)

            p = j = 0
            i = k = left

            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1

            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n
    _merge_sort(a, 0, n - 1)
    del buff


n = int(sys.stdin.readline())
x = []
for _ in range(n):
    x.append(int(sys.stdin.readline()))

merge_sort(x)

for i in x:
    print(i)
