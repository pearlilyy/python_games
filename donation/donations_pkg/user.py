def login(database, username, password):
    
    if username in database:
        if database[username] == password:
            print(f"Welcome back {username.capitalize()}!!\n")
            return username
        else:
            print(f"Incorrect password for {username}\n")
            return ""
    else:
        print(f"User '{username}' not found. Please register.\n")
        return ""

def register(database, username, password):
    # username 길이는 1~10까지로 지정
    if len(username) > 10 or len(username) <= 0:
        print("Username must not be longer than 10 character.\n")
        return ""
    # 비밀번호는 5~15까지로 지정
    elif len(password) < 5 or len(password) > 15:
        print("\nPassword must be at least 5 characters and not be over 15 characters\n")
        return ""
    else:
        # username이 데이터베이스에 이미 있다면 빈 값을 리턴하고 다시 돌아가기
        if username in database:
            print("\nUsername already registered. Enter a different username!\n")
            return ""
        else:
            print(f"\nUsername '{username}' registered!\n")
            return username
