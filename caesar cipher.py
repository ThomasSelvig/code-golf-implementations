print ((lambda set, text, key: "".join(set[int(set.find(i))+key % len(set)] for i in text))("abcdefghijklmnopqrstuvwxyz", input("Plaintext: "), int(input("Key: "))))
