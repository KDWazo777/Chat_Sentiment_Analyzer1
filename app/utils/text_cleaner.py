import re
import emoji

def clean_context(context):

    # Emoji conversion
    context = emoji.demojize(context)

    # Remove URLs
    context = re.sub(
        r'http\S+|www\S+|https\S+',
        '',
        context
    )

    # Remove mentions
    context = re.sub(
        r'@\w+',
        '',
        context
    )

    # Remove extra spaces
    context = re.sub(
        r'\s+',
        ' ',
        context
    ).strip()

    return context