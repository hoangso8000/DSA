#prob1
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
data = "dad and mamam mommy i love you chiu chiu huy huu uhu"
pl=list(map(lambda x:x.lower(),word_tokenize(data)))
palindromes = list(filter(lambda word: word == word[::-1], pl))
pl2=list(filter(lambda x: len(x)!=1, palindromes))
print(pl2)
#prob2
def mystery(a,b):
    if(a==0):
        return 0
    if a%2==0:
        return 2*mystery(a/2,b)
    return b+mystery((a-1)/2,b)
print(mystery(8,8))
# In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

# Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

# Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)
def shortestBrigde(A):


    rows, cols = len(A), len(A[0])
    visited = set()
    perimeter = set()


    def neighbor(r, c):
        if r != 0:
            yield (r-1, c)
        if r != rows-1:
            yield (r+1, c)
        if c != 0:
            yield (r, c-1)
        if c != rows-1:
            yield (r, c+1)


    def get_perimeter(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if A[r][c] == 0 or (r, c) in visited:
            return
        visited.add((r, c))
        for r1, c1 in neighbor(r, c):
            if A[r1][c1] == 0:
                perimeter.add((r1, c1))
            else:
                get_perimeter((r1, c1))


    for r in range(rows):
        for c in range(cols):
            if perimeter:
                break
            get_perimeter(r, c)
    steps = 1
    while True:
        new_perimeter = set()
        for r, c in perimeter:
            for r1, c1 in neighbor(r, c):
                if(r1, c1) in visited:
                    continue
                if A[r1][c1] == 1:
                    return steps
                new_perimeter.add((r1, c1))
        visited |= new_perimeter
        perimeter = new_perimeter
        steps += 1
        
shortestBrigde([[1,0],[0,1]])