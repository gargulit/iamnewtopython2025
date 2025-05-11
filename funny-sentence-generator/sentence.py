import random

subjects = ["My cat", "A pirate", "An alien", "My teacher", "A unicorn", "A potato"]
verbs = ["ate", "painted", "hugged", "sang to", "argued with", "threw"]
objects = ["a banana", "the moon", "a laptop", "a spaghetti monster", "my homework", "a donut"]
places = ["in the bathroom", "on the moon", "in class", "at the zoo", "under the bed", "in a volcano"]

subject = random.choice(subjects)
verb = random.choice(verbs)
obj = random.choice(objects)
place = random.choice(places)

print("Here's your funny sentence:")
print(f"{subject} {verb} {obj} {place}.")
