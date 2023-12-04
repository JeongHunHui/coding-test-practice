from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        chars = ['A','C','G','T']
        l = len(startGene)
        gene_set = set()
        valid_gene_set = set(bank)
        que = deque([[1,startGene]])
        while que:
            count, gene = que.popleft()
            for i in range(l):
                current_c = gene[i]
                left = gene[:i]
                right = gene[i+1:]
                for c in chars:
                    if c == current_c:
                        continue
                    new_gene = left+c+right
                    if new_gene not in valid_gene_set or new_gene in gene_set:
                        continue
                    if new_gene == endGene:
                        return count
                    gene_set.add(new_gene)
                    que.append([count+1, new_gene])
        return -1