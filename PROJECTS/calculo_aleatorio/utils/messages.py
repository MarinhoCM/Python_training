def sucess_message(text: str) -> str:
    message = (f'\033[32m{text}\033[0m')
    return message

def error_message(text: str) -> str:
    message = (f'\033[31m{text}\033[0m')
    return message

def operation_message(text: str) -> str:
    message = (f'\033[33m{text}\033[0m')
    return message
