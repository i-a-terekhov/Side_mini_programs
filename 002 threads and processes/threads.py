from threading import Thread
import time


class ThreadsExample(Thread):

    def __init__(self):
        super().__init__()
        self.results = []

    def run(self, rounds=10):
        threads = []
        for i in range(rounds):
            thread = Thread(target=self.one_process, args=(i,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        print("Сумма всех единиц от вычислений равна", sum(self.results))

    def one_process(self, i):
        print(f"Старт {i:3}")
        time.sleep(0.0001)
        x = (10000000 ** 1000000) / (10000000 ** 999999) - 10000000 + 1     # result == 1
        self.results.append(int(x))
        print(f"\t\t\tФиниш {i:3}")


started_at = time.time()
example = ThreadsExample()

example.run(1000)

ended_at = time.time()
elapsed = round(ended_at - started_at, 4)
print(f'Функция работала {elapsed} секунд(ы)')