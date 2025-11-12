spaces = "   ну але   "
replacement = "Я плохой тестер"
new_replacement = replacement.replace("плохой", "отличный")
my_split = "Python is great"
test_split = my_split.split()
my_join = ['вы', 'любите', 'розы']
test_join = " ".join(my_join)


print(spaces.strip())
print(new_replacement)
print(test_split)
print(test_join)