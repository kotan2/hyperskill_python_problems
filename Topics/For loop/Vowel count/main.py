string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

vowels_count = 0;

for c in string:
    if c in vowels:
        vowels_count += 1

print(vowels_count)