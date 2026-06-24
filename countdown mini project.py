import time

count = int(input("Enter the number you want to count down from: "))

print("\n Count starts now : " )

for num in range(count, 0, -1):
    print(num)
    time.sleep(1)

print("\n Happy Birthday Umar & Umair! ")
