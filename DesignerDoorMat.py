N,M="7 31".split(" ") ## M and N as ODD, M = 3*N
N,M=int(N),int(M)
base_pattern=".|."
matrix=[]
lines=[(3*i)+1 for i in range(M)]
print(lines)
for i in range(N):
    row=[]
    for j in range(M):
        if j in lines:
            row.append("|")
        else:
            row.append(".")
    matrix.append(row)
pattern_element="-"
number_elements=1
mid_point_row=int((N+1)/2)-1
mid_point_col=int((N+1)/2)-1
distance=int((M-1)/2)
counter=1
welcome_value=int((M-len("WELCOME"))/2)
welcome_string_left="".join(["-" for i in range(welcome_value)])
welcome_string_right="".join(["-" for i in range(welcome_value)])
welcome_string=welcome_string_left+"WELCOME"+welcome_string_right
print(welcome_string)
for row in range(N):
    if row<mid_point_row:
        for col in range(0,distance):
            matrix[row][col]=pattern_element
        for col in range(distance+counter,M):
            matrix[row][col]=pattern_element
        distance-=2
        counter+=2
    elif row==mid_point_row:
        matrix[row]=[welcome_string[i] for i in range(M)]
    else:
        print(row)
        reflection=mid_point_row-(row-mid_point_row)
        print(reflection)
        if reflection!=mid_point_row:
            matrix[row]=matrix[mid_point_row-(row-mid_point_row)]
for row in matrix:
    print("".join(row))

# mid_point=int(((N-1)/2)+1)
# welcome_mid=int(((M-1)/2)+1)
# welcome_start=welcome_mid-3
# welcome_end=welcome_mid+3
# output_dots=".|."