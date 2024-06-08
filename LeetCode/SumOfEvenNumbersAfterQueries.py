def sum_even_after_queries(self, nums, queries):
    even_sum_array = []
    even_sum = 0

    for number in nums:
        if number % 2 == 0:
            even_sum += number

    for query in queries:
        even_sum = even_sum - nums[query[1]] if nums[query[1]] % 2 == 0 else even_sum
        nums[query[1]] += query[0]
        even_sum = even_sum + nums[query[1]] if nums[query[1]] % 2 == 0 else even_sum
        even_sum_array.append(even_sum)

    return even_sum_array

