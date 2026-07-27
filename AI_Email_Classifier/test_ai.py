from classifier import classify_email


print(
    classify_email(
        "Amazon order delivered",
        "Your package has been shipped"
    )
)


print(
    classify_email(
        "HDFC transaction alert",
        "Money debited from account"
    )
)


print(
    classify_email(
        "Interview scheduled",
        "TCS recruitment team"
    )
)