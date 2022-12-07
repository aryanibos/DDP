import random

def indo():
    # fn = ["Park", "Han", "Kim", "Burhan","Seok", "Muhammad"]
    fn = ["Muhammad", "Al", "Riski", "Fathir", "Jidan"]
    ln = ["Fatih", "Alief", "Yudha","Saep"]
    # ln = ["Jong-un", "Ji-soo", "Is-lam","Doo-son"]
    firstName = random.choice(fn)
    lastName = random.choice(ln)
    name = firstName + " " +lastName
    print(name)

indo()