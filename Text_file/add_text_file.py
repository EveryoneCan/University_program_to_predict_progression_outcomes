# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20210113
#WOU ID: w1912800
# Date: 4/17/2022

def all_progression(list5,list4):
    #Create variables
    file=0
    add_element=0

    #Get the length of the list5
    length=len(list5)
    
    for elements in range(length):
        
        # Join the mark list without brackets
        file_output=list5[add_element]+" - "+(','.join(map(str,list4[add_element])))

        #Open the text file in append mode
        file = open("Progression results.txt", "a")
        add_element=add_element+1

       #Write the output in the file
        file.write(file_output+"\n")
        file.close()

    return
    
    
