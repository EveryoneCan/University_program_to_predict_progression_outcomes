# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20210113
#WOU ID: w1912800
# Date: 4/17/2022

def vertical(list2):
    #Print the results in vertical histogram
    progression1 = list2[0]
    progression2 = list2[1]
    progression3 = list2[2]
    progression4 = list2[3]

    print("\n\tVertical histogram")
    print("")
    header = ['Progress ', 'Trailing', 'Retriever', 'Excluded']
    print(' '.join(header))
    for x in range(max(progression1, progression2, progression3, progression4)):
        print(" {0}     {1}     {2}     {3}".format(
            '*    ' if x < progression1  else '     ',
            '*    ' if x < progression2  else '     ',
            '*    ' if x < progression3 else '     ',
            '*    ' if x < progression4  else ' '
        ))


    return
