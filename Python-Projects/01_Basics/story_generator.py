import random
names = [
    "Sasa", "Yasir", "Amina", "Rahil", "Neha", "Kiran", "Aditya", "Sara", "Zoya", "Vikram",
    "Tanvi", "Rohan", "Meera", "Kabir", "Ananya", "Arjun", "Ishaan", "Priya", "Dev", "Naina",
    "Kavya", "Sameer", "Tara", "Rishi", "Aarav", "Anika", "Jay", "Diya", "Veer", "Nisha"
]

verb_phrases = [
    "is running",
    "is jumping",
    "is swimming",
    "is eating",
    "is sleeping",
    "is writing",
    "is reading",
    "is playing",
    "is singing",
    "is dancing",
    "are walking",
    "are cooking",
    "are driving",
    "are thinking",
    "are laughing"
]


when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']

residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']

print(
    f"{random.choice(names)} {random.choice(verb_phrases)} {random.choice(when)}, "
    f"{random.choice(who)} in {random.choice(residence)} went to {random.choice(went)} and "
    f"{random.choice(happened)}."
)


