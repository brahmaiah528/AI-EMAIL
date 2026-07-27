import requests


def get_emails(access_token):

    url = (
        "https://graph.microsoft.com/v1.0/me/messages"
        "?$top=20"
        "&$select=id,subject,from,bodyPreview,"
        "receivedDateTime,isRead"
    )

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }


    response = requests.get(
        url,
        headers=headers
    )


    print("Status Code:", response.status_code)


    data = response.json()

    emails = []


    for mail in data.get("value", []):

        sender_name = "Unknown"
        sender_email = "Unknown"


        if mail.get("from"):

            email_data = mail["from"]["emailAddress"]

            sender_name = email_data.get(
                "name",
                "Unknown"
            )

            sender_email = email_data.get(
                "address",
                "Unknown"
            )


        emails.append(
            {
                "ID": mail.get("id"),

                "Sender": sender_name,

                "Email": sender_email,

                "Subject": mail.get(
                    "subject",
                    "No Subject"
                ),

                "Body": mail.get(
                    "bodyPreview",
                    ""
                ),

                "Date": mail.get(
                    "receivedDateTime",
                    ""
                ),

                "Status":
                "Read"
                if mail.get("isRead")
                else "Unread"
            }
        )


    return emails