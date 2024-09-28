#Objective
#Understand the concept and usage of immutable sets (frozen sets).
#The task

#Create a frozen set named frozen_set containing elements "hello", "world".
frozen_set = frozenset(["hello", "world"])

#Try to add "!" to frozen_set. What happens?
#frozen_set.add("!") # Frozen sets are immutable and you cannot add elements to them.

#Create a normal set named normal_set containing elements "let's", "learn".
normal_set = {"let's", "learn"}

#Try to add frozen_set to normal_set. Why does it work? Explain.
normal_set.add(frozen_set)  #this works because frozen sets are hashable and therefore can be elements of other sets
                            #Hashable objects have a fixed value, which allows them to be included in sets or used as dictionary keys.
                            #Regular sets are not hashable and cannot be added to other sets, but frozen sets can be.

#Print normal_set.
print(normal_set)

#Run your script half a dozen times. What do you notice about where frozen_set is added to normal_set? Hint: Look at the order of the items.
#the order of elements changes
#sets ( both normal and frozen ) are unordered collections

#What makes a frozen set different to a normal set? Explain.
#normal sets are mutable( u can add, remove, modify) --- frozen set are immutable
#normal sets :not hashable, so they cannot be added to other sets or used as dictionary keys.
# ---Frozen Sets: Hashable, so they can be added to other sets or used as dictionary keys.

