def unique_emails(my_emails):
    emails = [address.lower() for address in my_emails]
    emails = set(emails)
    return emails

emails = ['aa', 'b', 'Aa', 'a', 'bb', 'cc', 'c']
    
newemail = unique_emails(emails)
print(newemail)