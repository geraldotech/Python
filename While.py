while True:
    D = input('What is your decision, stand or hit? [press S for stand and H for hit]: ')
    if D not in ['S', 'H']:
        print('Incorrect input, please try again (S for stand and H for hit)!')
        continue
    else:
        if D == 'S':
            print('OK, you decided to stand!')
        else:
            print('OK, you decided to hit. You will receive a 3rd card!')
        break 