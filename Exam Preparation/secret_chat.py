def concealed_message(text):

    while True:
        command = input().split(':|:')
        if command[0] == 'Reveal':
            print(f"You have a new text message: {text}")
            break
        elif command[0] == 'InsertSpace':
            current_command, index = command[0], command[1]
            text = text[:int(index)] + " " + text[int(index):]
            print(text)
        elif command[0] == 'Reverse':
            current_command, substring = command[0], command[1]
            if substring in text:
                text = text.replace(substring, '', 1)
                text = text + substring[::-1]
                print(text)
            else:
                print("error")
        elif command[0] == 'ChangeAll':
            current_command, substring, replacement = command[0], command[1], command[2]
            text = text.replace(substring, replacement)
            print(text)

message = input()
concealed_message(message)