import time

while True:
    answer = int(input("Press 1 to generate new image or 2 to exit\n"))
    if answer == 1:
        with open('prng-service.txt', 'w') as outfile:
            outfile.write("Run")
            outfile.close()
            time.sleep(5)
        with open('prng-service.txt', 'r') as infile:
            rand_int = infile.readline()
            infile.close()
        with open('image-service.txt', 'w') as outfile:
            outfile.write(rand_int)
            outfile.close()
            time.sleep(5)
        with open('image-service.txt', 'r') as infile:
            path = infile.readline()
            print(path)
    elif answer == 2:
        break
    else:
        print("Not a valid choice")





