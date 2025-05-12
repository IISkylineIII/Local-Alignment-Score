def local_alignment_score(seq1, seq2, match_score, mismatch_penalty, indel_penalty):
    matrix = [[0] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]

    max_score = 0  # Keep track of the maximum score in the matrix
    max_i, max_j = 0, 0  # Keep track of the position of the maximum score

    # Fill in the matrix and find the maximum score position
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            if seq1[i - 1] == seq2[j - 1]:
                score = matrix[i - 1][j - 1] + match_score
            else:
                score = max(matrix[i - 1][j] - indel_penalty, matrix[i][j - 1] - indel_penalty, matrix[i - 1][j - 1] - mismatch_penalty, 0)

            matrix[i][j] = score

            if score > max_score:
                max_score = score
                max_i, max_j = i, j

    local_alignment_score = matrix[max_i][max_j]

    return local_alignment_score

seq1 = "A--ATAGCGACGCCTCGA"
seq2 = "CCGATA-CGATA-CATAGC"
match_score = 1
mismatch_penalty = 3
indel_penalty = 1

alignment_score = local_alignment_score(seq1, seq2, match_score, mismatch_penalty, indel_penalty)
print("Score of the bold portion of the local alignment:", alignment_score)
