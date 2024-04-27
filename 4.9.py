def sum_of_series():
    start = 3
    end = 30
    step = 3
    total = 0

   
    for num in range(start, end + 1, step):
        total += num

    return total

def main():
    series_sum = sum_of_series()
    print("Sum of the series 3 + 6 + 9 + ... + 30 is:", series_sum)

if __name__ == "__main__":
    main()
