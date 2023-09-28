love_banner = '''
  ___        _    _   _ ____  _    
 / _ \ _ __ / \  / \ | / ___|| |   
| | | | '__/ _ \| | | \___ \| |   
| |_| | | / ___ \ |_| |___) | |___
 \___/|_|/_/   \_\___/|____/|_____|
'''

print(love_banner)
print("Welcome to the Love Story Game!")
print("You are about to embark on a romantic adventure. Your choices will shape the story.")

name = input("Enter your character's name: ")
partner_name = input("Enter your partner's name: ")

print(f"Once upon a time, there was a person named {name} who fell in love with {partner_name}.")

choice1 = input(f"{name}, you meet {partner_name} at a cafe. Do you smile and say hi? (yes/no): ")

if choice1.lower() == "yes":
    print(f"{partner_name} smiles back and you strike up a conversation.")
    print("You both discover a shared interest in music.")
else:
    print(f"You hesitate and miss the opportunity to talk to {partner_name}.")

choice2 = input(f"{name}, you've been talking for a while. Do you ask {partner_name} for their phone number? (yes/no): ")

if choice2.lower() == "yes":
    print(f"{partner_name} happily gives you their phone number. You plan to meet again.")
    print("As time goes by, your love story deepens.")
    print(f"You go on dates, explore new places, and create beautiful memories with {partner_name}.")
    choice_commit = input(f"Do you decide to commit to a relationship with {partner_name}? (yes/no): ")
    if choice_commit.lower() == "yes":
        print(f"You and {partner_name} are officially a couple. Your love continues to grow.")
        print(f"{name}, you and {partner_name} have a bright future together.")
    else:
        print(f"You decide to remain friends with {partner_name}. Your bond remains strong but platonic.")
else:
    print(f"You decide not to ask for {partner_name}'s number. You part ways and never see each other again.")
    print(f"Years later, you still wonder what could have been with {partner_name}.")

print(f"{name}, your love story with {partner_name} has reached its conclusion.")
