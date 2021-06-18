class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0])%2 and int(coordinates[1])%2 == 0) or (ord(coordinates[0])%2 == 0 and int(coordinates[1])%2)
        
