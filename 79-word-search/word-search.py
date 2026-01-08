class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        L = len(word)

        for i in range(m):
            for j in range(n):
                if board[i][j] != word[0]:
                    continue

                stack = [(i, j, 0, set([(i, j)]))]

                while stack:
                    r, c, idx, visited = stack.pop()

                    if idx == L - 1:
                        return True

                    for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                        nr, nc = r + dr, c + dc
                        if (
                            0 <= nr < m and
                            0 <= nc < n and
                            (nr, nc) not in visited and
                            board[nr][nc] == word[idx + 1]
                        ):
                            stack.append(
                                (nr, nc, idx + 1, visited | {(nr, nc)})
                            )

        return False
