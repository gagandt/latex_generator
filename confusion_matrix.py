def print_conf_mat(M):
    print('\[')
    print('\\textbf{M } =  \left[ {\\begin{array}{ccc}')
    print(str(M[0][0]) + ' & ' + str(M[0][1]) + ' & ' + str(M[0][2]) + ' \\\\')
    print(str(M[1][0]) + ' & ' + str(M[1][1]) + ' & ' + str(M[1][2]) + ' \\\\')
    print(str(M[2][0]) + ' & ' + str(M[2][1]) + ' & ' + str(M[2][2]) + ' \\\\')
    print('\\end{array}} \\right]')
    print('\]')