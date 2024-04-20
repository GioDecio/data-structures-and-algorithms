import time
import random


def main():
    def has_duplicates_quadratic(array):

        for i, _ in enumerate(array):
            for j, _ in enumerate(array):
                if i != j and array[j] == array[i]:
                    return True

        return False

    def has_duplicates_linear(array):

        ex_numbers = []
        for i, n in enumerate(array):
            ex_numbers.append(n)
            if n in ex_numbers[:-1]:
                return True
        return False

    # Generate 5 random numbers between 10 and 30
    array = random.sample(range(10, 10**7), 10**6)

    # start_time = time.time()
    # print(f"Has duplicates - quadratic: {has_duplicates_quadratic(array)}")
    # print("Time taken: --- %.5f minutes --- \n" % ((time.time() - start_time) / 60))

    start_time = time.time()
    print(f"has duplicates - linear: {has_duplicates_linear(array)}")
    print("Time taken: --- %.5f minutes ---" % ((time.time() - start_time) / 60))


if __name__ == "__main__":
    main()
