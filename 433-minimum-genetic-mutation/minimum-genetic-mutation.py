class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        choices="ACGT"
        queue=deque([(startGene,1)])
        bank=set(bank)
        visited={startGene}
        while queue:
            gene,count=queue.popleft()
            if gene==endGene:
                return count-1
            for i in range(len(gene)):
                for choice in choices:
                    newgene=gene[:i]+choice+gene[i+1:]
                    if newgene in bank and newgene not in visited:
                       visited.add(newgene)
                       queue.append((newgene,count+1))
        return -1
                
        
        