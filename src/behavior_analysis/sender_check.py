def get_sender_domain(sender_email):

    if sender_email:
        return sender_email.split("@")[1]

    return None