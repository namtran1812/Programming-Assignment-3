import time
import subprocess

files = [
    "test/test1.in",
    "test/test2.in",
    "test/test3.in",
    "test/test4.in",
    "test/test5.in",
    "test/test6.in",
    "test/test7.in",
    "test/test8.in",
    "test/test9.in",
    "test/test10.in"
]
sizes = []
times = []

for file in files:
    with open(file, "r") as f:
        lines = f.readlines()
        strA = lines[-2].strip()
        strB = lines[-1].strip()
        size = len(strA) * len(strB)
        sizes.append(size)
    start = time.perf_counter()
    with open(file, "r") as f:
        subprocess.run(
            ["python3", "src/code.py"],
            stdin=f,
            stdout=subprocess.PIPE,
            text=True
        )
    end = time.perf_counter()
    times.append(end - start)
print("sizes =", sizes)
print("times =", times)