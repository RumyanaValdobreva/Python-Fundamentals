word = input()
lowcase_word = word.lower()

sand = lowcase_word.count('sand')
water = lowcase_word.count('water')
fish = lowcase_word.count('fish')
sun = lowcase_word.count('sun')

print(sand + water + fish + sun)