library = 200
to_be_removed = 47

new_list = library - to_be_removed

print(new_list)

movie_ticket = 12
no_of_tickets = 2

print(f"The total cost of the movie tickets is: ${movie_ticket * no_of_tickets}")

no_stickers = 48
no_of_friends = 6
stickers_per_friend = no_stickers // no_of_friends

print(f"Each friend will get {stickers_per_friend} stickers.")

hourly_rate = (int ("25"))
hours_worked =(int ("40"))

print(float((hourly_rate) * (hours_worked)))



name = input("What is your name? ")
age = input("What is your age? ")

question-one = what is competitive programming?



i have learnt how to use variables and some python syntax too

tasks = int(input("how many tasks were assigned to you today? "))
ack = str(input ("Did you complete the tasks assigned to you today? (yes/no) "))
left_over = int(input("If not, how many tasks are left over? "))


total_tasks_remaining = left_over
print(type(ack))


print(f"Tasks assigned: {tasks}")
print(f"Tasks completed: {ack}")
print(f"Tasks left over: {left_over}")
print(f"Total tasks remaining: {total_tasks_remaining}")


print("Thank you for providing the information. Have a great day!")

name = input("Hi! What is your name? ")
event = input("What was the event or occasion? ")
cost = float(input("How much was it? "))
service_charge = int(input("Was there a tip or a service charge? Enter a whole number (e.g. 20 for 20%): "))
group_size = int(input("How many people were in your group? "))


service_charge_amount = cost * (service_charge / 100)

total_cost = cost + service_charge_amount

total_cost_per_person = total_cost / group_size

print(f"Welcome to PayUp ! {name}")
print() 
print(f"Here's the breakdown for {event}:")
print()
print(f"Cost: ${cost}")
print(f"Service charges: ${service_charge}")
print(f"Group size: {group_size}")
print(f"Grand total: ${total_cost}")
print()
print(f"Each person must PayUp: ${total_cost_per_person}")