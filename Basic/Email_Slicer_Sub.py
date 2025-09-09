def emailProcess(email):
    email_username = email[0:email.index('@')]
    email_domain = email[email.index('@') + 1:]
    return [email_username, email_domain]


def printEmailInfo(email_username, email_domain):
    print(f'Your email username is: {email_username}')
    print(f'Your email domain is: {email_domain}')


def main():
    email = input("Enter your email address: ").strip()
    email_username, email_domain = emailProcess(email)


if __name__ == "__main__":
    main()
