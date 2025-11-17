firstName = input("Masukkan first name anda...")
lastName = input("Masukkan last name anda...")

# String concenation
print(firstName, lastName)
print(firstName + " " + lastName)
print(f"{firstName} {lastName}")
print("{} {}".format(firstName, lastName))

# Case modification
print(firstName.upper())
print(firstName.lower())
print(firstName.title())