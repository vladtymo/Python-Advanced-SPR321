# ------------ dictionaries ------------

users = {1200: "Vlad Tm", 555: "Nazar Bla", 9800: "Luda Buda"}

users[555] = "Viktor"

if 555 in users:
    print("Yes")
else:
    print("No")

for i in users:
    print(f"{i} - {users[i]}")

for key, val in users.items():
    print(f"{key} - {val}")

users.pop(1200)

print(f"Users: {len(users)}")

# ---------- hash function ----------
# initializing objects
int_val = 4
str_val = "GeeksforGeeks"
flt_val = 24.56

# Printing the hash values.
# Notice Integer value doesn't change
# You'll have answer later in article.
print("The integer hash value is : " + str(hash(int_val)))
print("The string hash value is : " + str(hash(str_val)))
print("The float hash value is : " + str(hash(flt_val)))
