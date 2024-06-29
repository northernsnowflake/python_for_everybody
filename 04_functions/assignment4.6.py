def computepay(h,r):
    if h <= 40:
        result = h * r
        return result
    if h > 40:
        result = (40 * r) + (h - 40) * r * 1.5 
        return result
    
hrs = input("Enter hours: ")
rate = input("Enter rate: ")

h = float(hrs)
r = float(rate)

p = computepay(h,r)
print("Pay",p)