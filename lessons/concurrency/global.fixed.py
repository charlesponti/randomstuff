import concurrent.futures
import threading

thread_local = threading.local()


def increment_counter(fake_value):
    if not hasattr(thread_local, "counter"):
        thread_local.counter = 0
    for _ in range(100):
        counter += 1


if __name__ == "__main__":
    fake_data = [x for x in range(5000)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(increment_counter, fake_data)
        # print(thread_local.counter)
