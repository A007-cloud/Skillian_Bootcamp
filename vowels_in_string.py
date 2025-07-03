def vowels_in_string(str):
    vowels = "aeiouAEIOU";
    if any(char in vowels for char in str):
        print('string do have vowels')
    else:
        print('string do not have vowles')

str = "helloWorld";
vowels_in_string(str);

