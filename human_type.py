import time

def human_type(element, text):
    for c in text:
        element.send_keys(c)
        time.sleep(0.1)