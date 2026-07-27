from classifier import classify_email


result = classify_email(
    "Amazon order shipped",
    "Your package has been delivered"
)

print(result)