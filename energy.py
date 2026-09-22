PLANCK_CONSTANT = 6.626e-34


def main():
    while True:
        try:
            frequency = float(input("Enter Frequency: "))
            if frequency > 0:
                break
            else:
                print("Frequency must be positive!")
        except ValueError:
            print("Invalid input, enter a number! ")

    energy = calculate_energy(frequency)
    print(f"Energy: {energy:.2e} Joules")


def calculate_energy(frequency):
    E = PLANCK_CONSTANT * frequency
    return E


if __name__ == "__main__":
    main()
