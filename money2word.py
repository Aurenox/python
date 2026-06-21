n = int(input("Enter Amount: "))

ones = ["", "One", "Two", "Three", "Four", "Five",
        "Six", "Seven", "Eight", "Nine"]

teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
         "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

tens = ["", "", "Twenty", "Thirty", "Forty",
        "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

if n == 10000:
    print("Ten Thousand")

else:
    if n >= 1000:
        print(ones[n // 1000], "Thousand", end=" ")
        n %= 1000

    if n >= 100:
        print(ones[n // 100], "Hundred", end=" ")
        n %= 100

    if 10 <= n <= 19:
        print("and", teens[n - 10])
    else:
        print("and", tens[n // 10], ones[n % 10])