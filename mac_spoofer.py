from generate_mac import generate_mac

opt0 = generate_mac.total_random() 
opt1 = generate_mac.total_random() 
opt2 = generate_mac.total_random() 
opt3 = generate_mac.total_random() 

print('Option 1: ' +opt0) 
print('Option 2: ' +opt1) 
print('Option 3: ' +opt2)
print('Option 4: ' +opt3)
print('Please choose a Mac Address option 1-4 as follows: ')

choice = input()

if choice == '1':
    print(opt0)
elif choice == '2':
    print(opt1)
elif choice == '3':
    print(opt2)
else:
    print(opt3)
    
print(choice)