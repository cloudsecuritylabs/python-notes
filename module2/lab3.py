# Write code that asks the user to provide a score for an exam as input and checks what
# grade the score is associated with. (Example: a score higher than 90 is an A.)
#81
test_score = float(input("Please enter your test score: "))
if test_score >= 90:
    print("A") # exit
elif test_score >= 80:
    print("B")
elif test_score >= 70:
    print("C")
else:
    print("Retake the exam")

# score >= 90-100 --> A
# score >= 80-89 --> B
# score >= 70-79 --> c
# score anything else --> retake the exam