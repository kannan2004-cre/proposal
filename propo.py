name = input("What's your loved one's name? ")
location = input("Where are you going to propose? ")
time = input("What time of day are you going to propose? ")
ring = input("Have you bought an engagement ring? ")

message = f"Dear {name},\n\nI hope this message finds you well. I wanted to take a moment to express how much you mean to me and how much I love you. I can't imagine my life without you in it.\n\n{location} at {time} is a special place and moment for us, and I would be honored if you would join me there once again. I have a question I want to ask you, and I hope you will say yes.\n\n{name}, will you marry me?{'' if ring.lower() == 'yes' else ' I also have an engagement ring that I hope you will love.'}\n\nWith all my love,\n[Your Name]"

print(message)
