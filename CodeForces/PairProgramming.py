test_cases = int(input())

def get_number_of_zeros(A):
    zeros = 0
    for i in range(len(A)):
        if A[i] == 0:
            zeros += 1
    return zeros


for _ in range(test_cases):
    k_lines_of_code, n_lines, m_lines = list(map(int, input().split()))
    n_changes = list(map(int, input().split()))
    m_changes = list(map(int, input().split()))
    total_changes = n_changes + m_changes
    max_zeros = get_number_of_zeros(n_changes) + get_number_of_zeros(m_changes)

    if k_lines_of_code + max_zeros < max(n_changes) or k_lines_of_code + max_zeros < max(m_changes):
        print("-1")
        break

    total_changes.sort();
    result_string = ""

    for i in range(len(total_changes)):
        if (total_changes[i] > k_lines_of_code):
            print("-1")
            break
        if i != len(total_changes) - 1:
            result_string += str(total_changes[i]) + " "
        else:
            result_string += str(total_changes[i])
        k_lines_of_code += 1

    print(result_string)