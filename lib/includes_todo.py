def includes_todo(text):
    if "#TODO" in text.upper():
        return True
    else:
        return False 