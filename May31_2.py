import sys

sys.stdin = open("in5.txt", "rt")
the_whole_input = sys.stdin
i_lines = the_whole_input.readlines()
testcase_cnt = int(i_lines[0])

sys.stdin = open("out5.txt", "rt")
the_whole_output = sys.stdin
o_lines = the_whole_output.readlines()

cnt = 1
for i in range(testcase_cnt):
    n, s, e, k = map(int, i_lines[2*cnt-1].split(sep=' '))
    # print(n, s, e, k)
    i_lines_list = i_lines[2*cnt].strip().split(' ')
    # print(i_lines_list)
    i_lines_int_list = list(map(int, i_lines_list))[s-1:e]
    # print(i_lines_int_list)
    output = sorted(i_lines_int_list)[k-1]

    if int(output) == int(o_lines[cnt-1].split(' ')[1]):
        print('정답')
    else:
        print('돌아가')

    cnt += 1
