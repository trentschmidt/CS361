import random

while True:
    with open('microservice.txt', 'r') as infile:
        status = infile.readline()
        infile.close()
        if status == "Day":
            random_int = random.randint(0, 1000)
            with open('microservice.txt', 'w') as outfile:
                outfile.write('%d' % random_int)
                outfile.close()
