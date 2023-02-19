class Tree:
  leaves = 285783
  height = 10
  age = 24
  name = "Pine"

  def __init__(self, type):
    self.type = type

  def get_older(self):
    self.age += 1
    self.leaves -= 147234
    self.height += 5


my_tree = Tree("Pine")

print(my_tree.age)
print(my_tree.leaves)
print(my_tree.height)
print(my_tree.name)

my_tree.get_older()
print(my_tree.age)
print(my_tree.leaves)
print(my_tree.height)
print(my_tree.name)




