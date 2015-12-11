import sys


class Bar:

    def __init__(self, expected_count):
        self._count = 0
        self._next_tic_count = 0
        self._tic = 0
        self._expected_count = expected_count
        sys.stdout.write(
            "0%   10   20   30   40   50   60   70   80   90   100%\n")
        sys.stdout.write(
            "|----|----|----|----|----|----|----|----|----|----|\n")
        if not self._expected_count:
            self._expected_count = 1

    def expected_count(self):
        return self._expected_count

    def count(self):
        return self._count

    def passed(self, num=1):
        self._count += num
        if self._count >= self._next_tic_count:
            self.update()

    def update(self):
        tics_needed = int(self._count * 50.0 / self._expected_count)
        sys.stdout.write('*')
        self._tic += 1
        while self._tic < tics_needed:
            sys.stdout.write('*')
            self._tic += 1
        self._next_tic_count = int(self._tic / 50.0 * self._expected_count)
        if self._count == self._expected_count:
            if self._tic < 51:
                sys.stdout.write('*')
            print '\n'


def main():
    import time
    count = 8
    pbar = Bar(count)
    for i in range(count):
        time.sleep(1)
        pbar.passed()

if __name__ == '__main__':
    main()
