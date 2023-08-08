import time 
def main():  
    print("Waiting 5 seconds. ") 
    for _ in range(5):
        name = input("What is your name")
        time.sleep(1)  
        print (f"Hello {name}")  
    print ("Finished waiting.")  
main() 