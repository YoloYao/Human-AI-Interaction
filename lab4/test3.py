# Stops inputting children if skip
if child_input in [ " skip " , " no " , " none " ]:
    have_child = False
# Due to URl formatting , the first child is 1 _ ( AGE ) , assigned using count , andthe subsequent ones are 2 C1_ ( AGE )
elif ( child_input . isdigit () ) :
    child_string += f " 1 _ { child_input } " if count < 1 else f " %2 C1_ { child_input } "
else :
    print ( " Sorry ! I don 't understand . What is the age of the child ? Or \" skip \"? ")