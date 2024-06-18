import time

count: int = 0
while True:
    print(count)
    count = count +1
    time.sleep(1)
    if count == 4:
        print("Oh Yeah")
        break
    

    
    
