
total_seconds =int(input("Enter total seconds:\n"))
hours=total_seconds//3600
remaining=total_seconds%3600
minute=remaining//60
seconds=remaining%60
print(f"{total_seconds} seconds is {hours} hours {minute} minute {seconds} seconds.")
