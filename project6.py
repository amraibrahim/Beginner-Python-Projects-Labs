import re
import random
from typing import Dict, List, Union

def normalizeEmail(emailIn: str) -> str:
    # Normalize the email address according to Gmail rules
    email = emailIn.lower()
    email = re.sub(r'\.(?=[^@]*@)|\+[^@]+', '', email)
    return email

def createDictionary(fileName: str) -> Union[Dict[str, int], str]:
    emailDict: Dict[str, int] = {}
    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            for line in file:
                email = normalizeEmail(line.strip())
                emailDict[email] = emailDict.get(email, 0) + 1
    except FileNotFoundError:
        return f"File cannot be opened: {fileName}"
    return emailDict

def getEligibleEmails(emailDictionary: Dict[str, int]) -> List[str]:
    return [email for email, count in emailDictionary.items() if count == 1]

def selectWinner(emailList: List[str]) -> str:
    if emailList:
        return random.choice(emailList)
    else:
        return "No eligible winners"


