
#preprocessing dataset
'''
          Harmless    Malicious   Suspicious
count  4813.000000  4813.000000  4813.000000
mean     50.210472     6.264908     0.498857
std      21.374932     4.864952     0.711391
min       0.000000     0.000000     0.000000
25%      55.000000     1.000000     0.000000
50%      58.000000     6.000000     0.000000
75%      62.000000    11.000000     1.000000
max      67.000000    23.000000     4.000000

'''
with open('C:\\Users\\marco\\Documents\\GitHub\\thesis-images\\scripts\\\classificator\\train_Dataset.csv', 'r') as f:
    dataset = f.read().split('\n')
    for l in dataset:
        if len(l) != 0:
            (classification,Harmless,Malicious,Suspicious)=l.split(',')
            #create bins for Harmless, Malicious and Suspicious
            if Harmless > 0 and Harmless < 20:
                Harmless = 0
            elif Harmless >= 20 and Harmless < 40:
                Harmless = 1
            elif Harmless >= 40 and Harmless < 60:
                Harmless = 2
            else:
                Harmless = 3

            if Malicious > 0 and Malicious < 20:
                Malicious = 0
            elif Malicious >= 20 and Malicious < 40:
                Malicious = 1
            elif Malicious >= 40 and Malicious < 60:
                Malicious = 2
            else:
                Malicious = 3
                
            print(','.join([classification,Harmless,Malicious,Suspicious]))

