def vowel_count(str):
    vowels='aeiouAEIOU'
    count=len([char for char in str if char in vowels])
    print(count)
str=input()
vowel_count(str)
