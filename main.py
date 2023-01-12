# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20210113
#WOU ID: w1912800
# Date: 4/17/2022

#importing os and clear the data that has in text file 
import os
if os.path.exists("Progression results.txt"):
  os.remove("Progression results.txt")

#Import python files
import Text_file.add_text_file
import Vertical_Outcome.vertical_star_outcome
import Horizontal_Outcome.horizontal_star_outcome

#Take a list and store the relavant outcomes given by university regulations
list2=[[120,0,0],[100,20,0],[100,0,20],[80,40,0],[80,20,20],[80,0,40],[60,60,0],[60,40,20],[60,20,40],[60,0,60],[40,80,0],[40,60,20],[40,40,40],[40,20,60],[40,0,80],[20,100,0],[0,80,20],[20,60,40],[20,40,60],[20,20,80],[20,0,100],[0,120,0],[0,100,20],[0,80,40],[0,60,60],[0,40,80],[0,20,100],[0,0,120]]

def student():

    #Create vriables
    progression1=0
    progression2=0
    progression3=0
    progression4=0

    #print the title that user have selected
    print("\n\tStudent Version \n")

    #While the condition gets true it iterates for the pass_credit
    while True:
        pass_credit=input("\nEnter your total PASS creits     : ")
        
        try:
            pass_credit=int(pass_credit)
            
            if pass_credit%20==0 and pass_credit<121:
                break

            else:
              print("Enter only one value from 20,40,60,80,100 or 120 to the pass credit as relevant")

        except ValueError:
            print("Please enter only integers")
    print("")

    #While the condition gets true it iterates for the defer_credit 
    while True:
        defer_credit=input("Enter your total DEEFER credits  : ")
        
        try:
            defer_credit=int(defer_credit)
            
            if defer_credit%20==0 and defer_credit<121:
                break

            else:
              print("Enter only one value from 20,40,60,80,100 or 120 to the defer credit as relevant")

        except ValueError:
            print("Please enter only integers")
    print("")
        
    #While the condition gets true it iterates for the fail_credit 
    while True:
        fail_credit=input("Enter your total FAIL credits    : ")
        
        try:
            fail_credit=int(fail_credit)

            if fail_credit%20==0 and fail_credit<121:
              break

            else:
              print("Enter only one value from 20,40,60,80,100 or 120 to the fail credit as relevant")

        except ValueError:
            print("Please enter only integers")
    print("")

    #Take the user input values to a list
    list1=[pass_credit,defer_credit,fail_credit]

    #If the user inputted marks are correct see the relavant outcome as the university required 
    if list1==list2[0]:
        outcome="progress"
        progression1=progression1+1

    if list1 in list2[1:3]:
        outcome="Progress (module trailer)"
        progression2=progression2+1

    if list1 in list2[4:14]:
        outcome="module retriever"
        progression3=progression3+1

    if list1==list2[14]:
        outcome="Exclude"
        progression4=progression4+1

    if list1 in list2[15:19]:
        outcome="module retriever"
        progression3=progression3+1

    if list1 in list2[19:21]:
        outcome="Exclude"
        progression4=progression4+1

    if list1 in list2[21:25]:
        outcome="module retriever"
        progression3=progression3+1

    if list1 in list2[24:28]:
        outcome="Exclude"
        progression4=progression4+1
          
    #If user input is in the progression print it
    if list1 in list2:
            print(outcome)

    #If total is incorrect re run the program
    else:
        print("""Total is incorrect
Please check your values again and enter only correct values""")
        student()

    return


def staff():

    #Create variables
    count=1
    progression1=0
    progression2=0
    progression3=0
    progression4=0
    x=0
    y=0
    list4=[]
    list5=[]
    elememt=0

    #Take a list and store the relavant outcomes given by university regulations
    list2=[[120,0,0],[100,20,0],[100,0,20],[80,40,0],[80,20,20],[80,0,40],[60,60,0],[60,40,20],[60,20,40],[60,0,60],[40,80,0],[40,60,20],[40,40,40],[40,20,60],[40,0,80],[20,100,0],[0,80,20],[20,60,40],[20,40,60],[20,20,80],[20,0,100],[0,120,0],[0,100,20],[0,80,40],[0,60,60],[0,40,80],[0,20,100],[0,0,120]]

    #print the title and the conditions to input data
    print("Staff Version with Histogram\n")
    print("""        Dear users please enter 20,40,60,80,100 or 120 
    to the pass credit,defer credit and fail credit as the relevant""")

    #The looping of the program to enter pass , fail and defer credits snd to display relavant outcome
    while count !=0:
        
        #While the condition gets true it iterates for the pass_credit  
        while True:
            pass_credit=input("\nEnter your total PASS creits     : ")
            
            try:
                pass_credit=int(pass_credit)

                if pass_credit%20==0 and pass_credit<121:
                    break

                else:
                    print("Enter only one value from 20,40,60,80,100 or 120 to the pass credit as relevant")

            except ValueError:
                print("Please enter only integers")
        print("")

        #While the condition gets true it iterates for the defer_credit 
        while True:
            defer_credit=input("Enter your total DEEFER credits  : ")
            
            try:
                defer_credit=int(defer_credit)
            
                if defer_credit%20==0 and defer_credit<121:
                    break

                else:
                    print("Enter only one value from 20,40,60,80,100 or 120 to the defer credit as relevant")

            except ValueError:
                print("Please enter only integers")
        print("")
        
        #While the condition gets true it iterates for the fail_credit 
        while True:
            fail_credit=input("Enter your total FAIL credits    : ")
            
            try:
                fail_credit=int(fail_credit)
                if fail_credit%20==0 and fail_credit<121:
                    break

                else:
                    print("Enter only one value from 20,40,60,80,100 or 120 to the fail credit as relevant")

            except ValueError:
                print("Please enter only integers")

        print("")

        #Take pass , defer and fail credits to a list        
        list1=[pass_credit,defer_credit,fail_credit]

        #Take relavant progression outcome to a variable from a list
        if list1==list2[0]:
            outcome="progress"
            progression1=progression1+1

        if list1 in list2[1:3]:
            outcome="Progress (module trailer)"
            progression2=progression2+1

        if list1 in list2[4:14]:
            outcome="module retriever"
            progression3=progression3+1

        if list1==list2[14]:
            outcome="Exclude"
            progression4=progression4+1

        if list1 in list2[15:19]:
            outcome="module retriever"
            progression3=progression3+1

        if list1 in list2[19:21]:
            outcome="Exclude"
            progression4=progression4+1

        if list1 in list2[21:25]:
            outcome="module retriever"
            progression3=progression3+1

        if list1 in list2[24:28]:
            outcome="Exclude"
            progression4=progression4+1
          
        #If total greater than 120 display total is incorrct and iterate
        if list1 in list2:
            print(outcome)
            list5.append(outcome)

        else:
            print("Total is incorrect")
            continue 

        #Appendng lists
        list4.append(list1)
        x=x+1

        #Ask user whether he want to add data again or not
        while True:
            print("\n\nWould you like to enter another set of data? ")
            user=input("Enter 'y' for yes or 'q' to quit and view results : ")
            
            try:
                if user.lower()=="y":
                    count=count+1
                    break
               
                if user.lower()=="q":
                  #Input a letter to give the results in which format
                  print("""\na. Print the results in horizontal histogram with stars and 
   show the appropriate results with the progression name and marks.
  \nb. Print the results in horizontal histogram with stars and show the
   appropriate results with the progression name and marks.Insteed
   of that print the results in vertical histogram.
  \nc. Print the results in horizontal histogram with stars and show the
   appropriate results with the progression name and marks.Insteed
   of that print the results in vertical histogram. As well as show
   results in a text file""")

                  #While user enters a correct letter it iterates the program
                  while True:
                      try:
                          letter=input("\nIn which kind of way do you want results? ")

                      except ValueError:
                          print ("Error")
                      
                      else:

                          if letter.lower()=="a":
                            
                              #Calling a file to print relavant user input
                              Horizontal_Outcome.horizontal_star_outcome.horizontal(progression1,progression2,progression3,progression4)
                              print("")

                              #Take the length of the list
                              length=len(list5)

                              #Print list4 and list5 seperately
                              for elements in range(length):
                                  print(list5[elememt]+" - "+(','.join(map(str,list4[elememt]))))
                                  elememt=elememt+1

                              #Count the total outcomes and print it
                              total=count
                              print("\n",total," outcomes in total.")

                              #Print a line after total outcomes
                              print("\n-----------------------------------------------------------\n")
                              break


                                
                          if letter.lower()=="b":

                              #Calling a file to print relavant user input
                              Horizontal_Outcome.horizontal_star_outcome.horizontal(progression1,progression2,progression3,progression4)
                              print("")
                              
                              #Take the length of the list  
                              length=len(list5)

                              #Print list4 and list5 seperately
                              for elements in range(length):
                                  print(list5[elememt]+" - "+(','.join(map(str,list4[elememt]))))
                                  elememt=elememt+1

                              #Count the total outcomes and print it
                              total=count
                              print("\n",total," outcomes in total.")
                              print("\n-----------------------------------------------------------\n")
                            
                              #Make a list to store data in horizontal histogram
                              list2=[progression1,progression2,progression3,progression4]
                               
                                
                              #Calling the function to print stars in vertically
                              Vertical_Outcome.vertical_star_outcome.vertical(list2)
                              total=count
                              print("\n",total," outcomes in total.")
                              print("\n-----------------------------------------------------------\n")
                              break

                          if letter.lower()=="c":

                              #Calling a file to print relavant user input
                              Horizontal_Outcome.horizontal_star_outcome.horizontal(progression1,progression2,progression3,progression4)
                              print("")

                              #Take the length of the list  
                              length=len(list5)

                              #Print list4 and list5 seperately
                              for elements in range(length):
                                  print(list5[elememt]+" - "+(','.join(map(str,list4[elememt]))))
                                  elememt=elememt+1

                              #Count the total outcomes and print it
                              total=count
                              print("\n",total," outcomes in total.")
                              print("\n-----------------------------------------------------------\n")
                            
                                
                                
                              #Make a list to store data in horizontal histogram
                              list2=[progression1,progression2,progression3,progression4]
                                
                                
                              #Calling the function to print stars in vertically
                              Vertical_Outcome.vertical_star_outcome.vertical(list2)
                              total=count
                              print(total," outcomes in total.")
                              print("\n-----------------------------------------------------------\n")
                            
                              
                              #Calling the function to open text file and display outcomes in it
                              Text_file.add_text_file.all_progression(list5,list4)
                              break
                            
                  if count!=0:
                    count=0
                    break
                
            except:
                pass
    return

#Get the user's input at the very first part
while True:
  
  try:
    print("\t\nDear user please enter a number from these as your required")
    print("""\n1. Student version
2. Staff version
3. Exit from the program""")
    
    choice=input("\nPlease enter your choice : ")
  except ValueError:
    print ("Error")
  else:
    if choice=="1":
      student()
      
    elif choice=="2":
      staff()
     
    elif choice=="3":
      break
    
    else:
     print ("Out of range")

