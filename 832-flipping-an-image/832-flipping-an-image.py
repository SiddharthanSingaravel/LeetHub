class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for ind_i, i in enumerate(image):
            image[ind_i] = image[ind_i][::-1]
            for ind_j, j in enumerate(image[ind_i]):
                image[ind_i][ind_j] = abs(1 - j)
        
        return image