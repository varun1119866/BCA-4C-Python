def sum_of_series():
    start = 4
    end = 40
    step = 4
    total = 0

   
    for num in range(start, end + 1, step):
        total += num

    return total

def main():
    series_sum = sum_of_series()
    print("Sum of the series 4 + 8 + 12 + ... + 40 is:", series_sum)

if __name__ == "__main__":
    main()
