import math 
# function to check minimum number of 
# digits should be removed to make 
# this number a perfect square 
def perfectSquare(s) : 
      
    # size of the string 
    n = len(s) 
  
    # our final answer 
    ans_square = -1
    ans_cube=-1
  
    # to store string which is 
    # perfect square and cube 
    num_square = "" 
    num_cube=""
  
    # We make all possible subsequences 
    for i in range(1, (1 << n)) : 
        str = "" 
        for j in range(0, n) : 
              
            # to check jth bit is 
            # set or not. 
            if ((i >> j) & 1) : 
                str = str + s[j] 
        # we do not consider a number  
        # with leading zeros 
        if (str[0] != '0') : 
              
            # convert our temporary  
            # string into integer 
            temp = 0; 
            for j in range(0, len(str)) : 
                temp = (temp * 10 + 
                 (ord(str[j]) - ord('0'))) 
  
            k = int(temp**(1/2))
            # checking temp is perfect  
            # square or not. 
            if (k * k == temp) : 
                  
                # taking maximum sized 
                # string 
                if (ans_square < len(str)) : 
                    ans_square = len(str) 
                    num_square = str
        if (str[0] != '0') : 
              
            # convert our temporary  
            # string into integer 
            temp = 0; 
            for j in range(0, len(str)) : 
                temp = (temp * 10 + 
                 (ord(str[j]) - ord('0')))
            m=math.ceil((temp**(1/3)))
            if (m*m*m==temp):
                if(ans_cube<len(str)): 
                    ans_cube=len(str)
                    num_cube=str
                    
                    
    if (ans_square == -1 and ans_cube==-1) : 
        return ans_square
    else :          
          
        # print PerfectSquare 
        print ("{} ".format(num_square), end="\n") 
        print ("{}".format(num_cube), end="\n")
        return n-ans_square, n-ans_cube
# Driver code 
print (perfectSquare("71254")) 
