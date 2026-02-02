# Định nghĩa node cho Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# ---- HÀM PHỤ ĐỂ TEST ----
def build_linked_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next


def print_linked_list(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(" -> ".join(res))


# ---- MAIN ----
if __name__ == "__main__":
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])

    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)

    print("Kết quả:")
    print_linked_list(result)
