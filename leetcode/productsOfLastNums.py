class ProductOfNumbers:
    def __init__(self):
        self.nums = []

    def add(self, num: int):
        self.nums.append(num)

    def getProduct(self, k: int) -> int:
        product = 1
        for i in range(abs(len(self.nums)) - k, len(self.nums)):
            product *= self.nums[i]
        return product


product = ProductOfNumbers()
product.add(3)
print(product.nums)  # Check if nums contains [3]
product.add(0)
print(product.nums)  # Check if nums contains [3, 0]
product.add(2)
print(product.nums)  # Check if nums contains [3, 0, 2]
product.add(5)
print(product.nums)  # Check if nums contains [3, 0, 2, 5]
product.add(4)
print(product.nums)  # Check if nums contains [3, 0, 2, 5, 4]
print(product.getProduct(2)) # 20
