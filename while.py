def run ():
    
    i= 1
    LIMITE=1000

    while i < LIMITE:
        print(i)
        i += 1
        if i == 333:
            print('333 llegamos a un numero con todos igual ')
            break
        
if __name__ == '__main__':
    run()