l = ["bat", "cat", "rat", "dat", "hat"]
m = ["bat", "cat", "fat", "hat", "mat", "pat", "rat", "sat", "vat", "wat"]

print(l)
print(m)

for word in l:
    print(f"current word: {word}")
    if word in m:
        l.remove(word)
        print(f"removed {word}")

print(l)
