
def count_vowels(str):
    vowels ="aeiouAEIOU";
    count = 0;
    for char in str:
        if char in vowels:
            count += 1;
    print(count);
count_vowels("HELLOWORLD");
