s = "datacamp"
dictionary = {}.fromkeys(["data", "camp", "now", "cam", "lack"])


def check(s):
    new_s = s
    for i in range(1, len(s)):
        print("sss :", s, i)
        string = s[:i]
        print(string)
        if string in dictionary:
            new_s = s[i:]
            if not new_s or new_s in dictionary or check(new_s):
                return True

    return False


print(check(s))
