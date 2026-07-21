from app.auth import hash_password, verify_password

password = "Akash123"

hashed = hash_password(password)

print("Original Password :", password)
print("Hashed Password   :", hashed)
print("Verify Password   :", verify_password(password, hashed))