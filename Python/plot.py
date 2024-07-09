def ploting(filepath):
    with open(filepath, 'r') as Input:
        lines = Input.readlines()
    time = []
    ch1 = []
    ch2 = []
    ch3 = []
    ch4 = []
    ch1_max = 0
    ch2_max = 0
    ch3_max = 0
    ch4_max = 0
    theshold = 0.072
    enable = False
    for line in lines:
        if (enable):
            data = line.split(',')
            #print(data)
            try:
                time.append(float(data[0])*100000000)
                ch1.append((float(data[1])))
                ch2.append((float(data[2])))
                ch3.append((float(data[3])))
                data[4] = data[4][:-1]
                ch4.append(float(data[4]))
                if ch1_max < abs(float(data[1])):
                    ch1_max = abs(float(data[1]))
                if ch2_max < abs(float(data[2])):
                    ch2_max = abs(float(data[2]))
                if ch3_max < abs(float(data[3])):
                    ch3_max = abs(float(data[3]))
                if ch4_max < abs(float(data[4])):
                    ch4_max = abs(float(data[4]))
            except:
                pass 
        if line.startswith('TIME'):
            enable = True
    #debug print the content
    # print(string)
    # print(time)
    # print(ch1)
    # print(len(ch2))
    # print(len(ch3))

    # double check for the maximum of the data
    # print('ch1 max: ', ch1_max)
    # print('ch2 max: ', ch2_max)
    # print('ch3 max: ', ch3_max)
    # print('ch4_max: ', ch4_max)
    trigger = False
    if ch3_max >= theshold or ch2_max >= theshold or ch4_max >= theshold:
        trigger = True
    else:
        trigger = False
    return trigger
    #plt.plot(time,ch1, alpha=0.75,c='y')
    #plt.plot(time,ch2, alpha=0.5,c='b')
    #plt.plot(time,ch3, alpha=0.25, c='r')
    #plt.savefig(fig)
#filenum = input('Enter the file number: ')

#filename = '../data/tek00' + filenum + '.csv'
#ploting(filename)
