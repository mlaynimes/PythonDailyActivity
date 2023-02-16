is_short = False
is_white = True

if is_short and is_white:
    print("You are short and white")

elif is_short and not(is_white):
    print("You are short and not a white")
elif not(is_short) and is_white:
    print("You are a white and not short")
else:
    print("you are not a short and white")