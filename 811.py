class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainDict = {}
        for domains in cpdomains:
            domain = domains.split(' ')
            subDomain = domain[1].split('.')
            tempStr = ''
            firstVar = True
            for x in range(len(subDomain) - 1,-1,-1):
                if firstVar:
                    tempStr = subDomain[x]
                    firstVar = False
                else:
                    tempStr = subDomain[x] + '.' + tempStr
                if tempStr in domainDict:
                    domainDict[tempStr] = int(domainDict[tempStr]) + int(domain[0])
                else:
                    domainDict[tempStr] = int(domain[0])
        output = []
        print(domainDict)
        for dicts in domainDict:
            output.append(str(domainDict[dicts]) + " " + dicts)
        return output
