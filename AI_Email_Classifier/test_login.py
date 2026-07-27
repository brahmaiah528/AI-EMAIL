from auth import login
from graph_api import get_emails


result = login()

if "access_token" in result:

    print("Login Successful")

    token = result["access_token"]

    emails = get_emails(token)

    print("\nYour Emails:\n")

    for email in emails:
        print("--------------------------------")
        print("Sender:", email["Sender"])
        print("Subject:", email["Subject"])
        print("Date:", email["Date"])
        print("Body:", email["Body"])

else:
    print("Authentication Failed")
    print(result)