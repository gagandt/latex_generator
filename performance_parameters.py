def print_per_para(M):
    hsum = [0,0,0]
    r = [0,0,0]
    p = [0,0,0]

    for j in range(0,3):
        h = 0
        v = 0;
        for i in range(0,3):
            h += M[j][i];
            v += M[i][j];
        
        hsum[j] = h;
        r[j] = M[j][j]*1.0/h*1.0
        p[j] = M[j][j]*1.0/v*1.0
    
    print('\\begin{table}[h!]')
    print('\\begin{center}')
    print('\\caption{ }')
    print('\\label{tab:table1}')
    print('\\begin{tabular}{l|c|c|r} % <-- Alignments: 1st column left, 2nd middle and 3rd right, with vertical lines in between')
    print('\\textbf{class} & \\textbf{Recall} & \\textbf{Precision} & \\textbf{F-Measure}\\\\')
    print('\\hline')
    print('class-1 &' + str(round(r[0], 2)) +' & ' + str(round(p[0], 2)) + ' & '+ str(round(2.0/(1.0/r[0] + 1.0/p[0]), 2)) +'\\'+'\\')
    print('class-2 &' + str(round(r[1], 2)) +' & ' + str(round(p[1], 2)) + ' & '+ str(round(2.0/(1.0/r[1] + 1.0/p[1]), 2)) +'\\'+'\\')
    print('class-3 &' + str(round(r[2], 2)) +' & ' + str(round(p[2], 2)) + ' & '+ str(round(2.0/(1.0/r[2] + 1.0/p[2]), 2)) +'\\'+'\\')
    print('\\end{tabular}')
    print('\\end{center}')
    print('\\end{table}')
    print('$\\mathbf{Accuracy}$ '+ str(round(float(M[0][0] + M[1][1] + M[2][2])/float(hsum[1] + hsum[2] + hsum[0]),2))+ '$\\%,$ $\\mathbf{Mean -Precision}$ ' + str(round((p[0] + p[1] + p[2])/3.0,2)) + '$,$ $\\mathbf{Mean -Recall}$ ' + str(round((r[0] + r[1] + r[2])/3.0,2))  + '$.$\\')
 