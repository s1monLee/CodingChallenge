class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = itemgetter(1), reverse = True)
        #boxTypes.sort(key=lambda boxType: boxType[1], reverse=True)
        unit =0
        for box in boxTypes:
            if truckSize >= box[0]:
                unit += box[0]*box[1]
                truckSize -= box[0]
            else:
                unit += truckSize * box[1]
                break
        return unit
