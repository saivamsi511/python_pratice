n = int(input().strip())
arr = list(map(int,input().strip().split()))
s = int(input().strip())

if s < 1 or s > n:
    print("Invalid start")

else:
    visited = set()
    steps = 0
    pos = s

    while True:
        if pos < 1 or pos > n:
            print(f"Exited in {steps} steps")
            break
        if pos in visited:
            print(f"Loop detected after {steps} steps")
            break
        visited.add(pos)
        pos += arr[pos-1]
        steps += 1