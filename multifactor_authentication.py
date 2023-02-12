import smtplib

"""
This script illustrates how MFA can be triggered when a user's account is logged in from a different location

"""


def trigger_2fa(email, location):
    """
    Triggers 2FA when an account is logged in from a different location.
    
    Keyword arguments:
    email -- the email address associated with the account
    location -- the location from where the account is being logged in
    """
    # Check if the location is different from the previously recorded location
    # Replace this code with your own logic for checking the location
    prev_location = "San Francisco"
    if location != prev_location:
        # Send an email to the user with a code for 2FA
        code = "123456"  # Replace this with a code generated by your 2FA solution
        message = "Your account has been logged in from a different location.\n"
        message += "Please enter the following code to complete the 2FA process: " + code
        subject = "Two-Factor Authentication Required"
        send_email(email, subject, message)


def send_email(to, subject, message):
    """
    Sends an email to the specified recipient.
    
    Keyword arguments:
    to -- the email address of the recipient
    subject -- the subject of the email
    message -- the message of the email
    """
    sender = "noreply@example.com"
    gmail_user = "example@gmail.com"
    gmail_password = "password"
    
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sender, to, f"Subject: {subject}\n\n{message}")
        server.close()
        print(f"Email sent to {to}")
    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == '__main__':
    # Example usage
    email = "user@example.com"
    location = "London"
    trigger_2fa(email, location)
