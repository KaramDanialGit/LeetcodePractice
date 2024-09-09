class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Calculate the length of the linked list
        n = 0
        curr = head
        while curr:
            n += 1  # Increment the length correctly
            curr = curr.next

        # Step 2: Determine the base size and how many parts need an extra node
        base = n // k  # Minimum size of each part
        extra = n % k  # Number of parts that get an extra node

        # Step 3: Split the linked list
        res = []
        curr = head
        for i in range(k):
            part_head = curr  # This is the head of the current part
            part_size = base + (1 if extra > 0 else 0)  # Add 1 more node to the first 'extra' parts
            extra -= 1  # Decrease extra after assigning an extra node

            # Now, advance the pointer `part_size - 1` steps to get to the end of the current part
            for _ in range(part_size - 1):
                if curr:
                    curr = curr.next

            # After advancing, break the current part if necessary
            if curr:
                next_part = curr.next  # The head of the next part
                curr.next = None  # Break the list here
                curr = next_part  # Move to the next part

            res.append(part_head)  # Add the head of the current part to the result

        return res