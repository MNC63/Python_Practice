from Email_Slicer_Sub import emailProcess, printEmailInfo


def main():
    emails = ['nhuptq@gmail.com', '1958028@itec.hcmus.edu.vn']
    for email in emails:
        username, email_domain = emailProcess(email)
        printEmailInfo(username, email_domain)


if __name__ == "__main__":
    main()
