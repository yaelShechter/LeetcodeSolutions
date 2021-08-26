    def my_sqrt(x: int) -> int:
        low = 1
        high = x
        mid = (low + high) // 2
        while True:
            if mid * mid <= x and x < (mid + 1) * (mid + 1):
                return mid
            if mid * mid > x:
                high = mid
                mid = (mid + low) // 2
            else:
                low = mid
                mid = (mid + high) // 2
