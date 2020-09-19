def printMode(a, n) :  
    max_element = max(a)
    t = max_element + 1
    count = [0] * t
    for i in range(t) :
        count[i] = 0
 
    for i in range(n) :
        count[a[i]] += 1
        
    mode = 0
    k = count[0]
    for i in range(1, t) : 
        if (count[i] > k) :
            k = count[i]
            mode = i
          
    print("mode = ", mode) 
  

if __name__ == "__main__" :
      
    a = [93,84,97,98,100,78,86,100,85,92,55,91,90,75,94,83,60,81,95,66]
    n = len(a)
    printMode(a, n)
