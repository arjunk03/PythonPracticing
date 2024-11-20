from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed
import urllib.request
import time


url_list = [
    "http://www.google.com/",
    "http://gmail.com/",
    "http://wikipedia.org/",
    "https://en.unesco.org/",
]


def url_loader(url, time):
    with urllib.request.urlopen(url, timeout=time) as conn:
        return conn.read()


def main_process_pool():
    start = time.time()

    with ProcessPoolExecutor(max_workers=7) as exec:
        future_to_page = {exec.submit(url_loader, url, 2): url for url in url_list}

        for future in as_completed(future_to_page):
            url = future_to_page[future]
            result = future.result()
            print("the page %r  is %d bytes" % (url, len(result)))

    print("total time taken : ", time.time() - start)


if __name__ == "__main__":
    main_process_pool()
