def semordnilap(str1,str2):
    if len(str1)!=len(str2):
        return False
    elif str1=='':
        return True
    else:
        return str1[0]==str2[-1] and semordnilap(str1[1:],str2[:-1])