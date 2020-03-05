from pprint import pprint
from collections import defaultdict

sentence = "A person is someone but written in a different way."
# words = sentence.split(" ")
# results = dict()

# for word in sorted(words):
#     first_letter = word[0]
#     if first_letter in results:
#         results[first_letter].append(word)
#     else:
#         results[first_letter] = [word]

# pprint(results)

words = sentence.split(" ")
results = defaultdict(list)

for word in sorted(words):
    first_letter = word[0]
    results[first_letter].append(word)

pprint(results)

# output:
# {
#     "a": ["A"],
#     "b": ["but"]
# }