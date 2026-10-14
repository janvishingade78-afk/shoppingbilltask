
#name:janvi shingade
#shopping bill task


def calculateElectronicsGST(a,b):
    subtotal=a+b
    return subtotal + (subtotal* 18/100)

def calculateFashionGST(c,d):
    subtotal=c+d
    return subtotal+(subtotal*13/100)

def calculateFoodGST(e):
    return e + (e * 7 / 100)


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return electronics + fashion + food


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    return total - discount


# Sample values given in the assignment
a = 100
b = 100
c = 100
d = 100
e = 100

electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)

print(f"Electronics after GST = Rs. {electronics:.2f}")
print(f"Fashion after GST = Rs. {fashion:.2f}")
print(f"Food after GST = Rs. {food:.2f}")
print(f"Total after GST = Rs. {total:.2f}")
print(f"Discount (20%) = Rs. {discount:.2f}")
print(f"Final payable amount = Rs. {final_amount:.2f}")