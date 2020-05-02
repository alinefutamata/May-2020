# Agree or Disagree

question = input("Do you agree? ").upper()

if question == "Y":
    print("You agreed")
elif question == "N":
    print("You Disagreed")
else:
    print("Please answer 'Y' for yes and 'N' for no")

