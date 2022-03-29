import uuid

def generateShortId():
    return uuid.uuid4().hex[:5]