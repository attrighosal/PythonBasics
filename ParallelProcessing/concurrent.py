import concurrent.futures

def job():
    print("Hi")

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(job) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())