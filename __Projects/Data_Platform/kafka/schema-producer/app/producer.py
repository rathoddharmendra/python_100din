import time

def main():
    print("Starting producer...")
    counter = 0
    while True:
        print(f"Produced message #{counter}")
        counter += 1
        time.sleep(2)

if __name__ == "__main__":
    main()
