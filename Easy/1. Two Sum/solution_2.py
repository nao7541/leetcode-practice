class Solution:
    def twoSum(self, nums, target):
        numToIndex = {}
        for i in range(len(nums)):
            # 辞書のキー存在チェック:
            # 辞書（ハッシュマップ）におけるキーの存在チェックは、ハッシュ関数を使用してキーのハッシュ値を計算し、
            # そのハッシュ値に対応するバケットを直接参照するため、平均的には O(1) の時間で実行されます。
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
        return []

# Time complexity: O(n)
# Space complexity: O(n)

def main():
    # テストケース
    nums = [3,2,4]
    target = 6
    # Solutionクラスのインスタンスを作成
    solution = Solution()
    # twoSumメソッドを呼び出して結果を取得
    result = solution.twoSum(nums, target)
    # 結果を表示
    print("Indices:", result)

if __name__ == "__main__":
    main()