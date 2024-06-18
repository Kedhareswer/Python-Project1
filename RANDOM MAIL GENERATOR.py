import random
domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l"]

def get_one_random_domain(domains):
        return domains[random.randint( 0, len(domains)-1)]


def get_one_random_name(letters):
    email_name = ""
    for i in range(7):
        email_name = email_name + letters[random.randint(0,11)]
    return email_name

def generate_random_emails():

    for i in range(0,10):
         one_name = str(get_one_random_name(letters))
         one_domain = str(get_one_random_domain(domains))         
         print(one_name  + "@" + one_domain)

def main():                
    generate_random_emails()