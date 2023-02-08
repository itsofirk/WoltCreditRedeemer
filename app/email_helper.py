import re
import PyPDF2 as pdf


def extract_code(message, pattern, group):
    """
    Extracts the code from the gift card.
    This function searches, using a pdf reader, in all the attachments, for a given regex for the code.

    :param message: the email message object
    :param pattern: the regex pattern to extract the code with
    :param group: what is the group number within the pattern to return
    :return: The gift card's code as a string
    """
    for attachment in message['attachments']:
        with open(attachment, 'rb') as f:
            reader = pdf.PdfFileReader(f)
            pageObj = reader.getPage(0)
            text = pageObj.extractText()
        res = re.search(pattern, text)
        if res:
            return res.group(group)


def filter_messages(messages, sender, subject):
    """
    Iterates over a messages iterable and filters for messages with a specific subject and sender.

    :param messages: iterable of message objects
    :param sender: desired sender (or part of it).
    :param subject: desired subject (or part of it).
    :return: generator, filtered messages.
    """
    for mid_email, message in messages.items():
        if sender in mid_email and subject in message['Subject']:
            yield message
    return

