# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=[]
        num2=[]
        ans=[]
        while l1 is not None:
            num1.append(l1.val)
            l1=l1.next
        while l2 is not None:
            num2.append(l2.val)
            l2=l2.next
        par=0
        if len(num1)>=len(num2):
            for a in range(len(num1)):
               
                sum=num1[a]+par
                if a<=len(num2)-1:
                    sum+=num2[a]
                print(sum)
                if sum>=10:
                    num1[a]=sum%10
                    par=1
                else:
                    num1[a]=sum
                    par=0
            if par==1:
                num1.append(par)
            ans_list=[]
            print(num1)
            for a in num1:
                ans_list.append(ListNode(val=a,next=None)) 
            for a in range(len(ans_list)-1):
                ans_list[a].next=ans_list[a+1]
            return ans_list[0]
        else:
            for a in range(len(num2)):
                
                sum=num2[a]+par
                if a<=len(num1)-1:
                    sum+=num1[a]
                if sum>=10:
                    num2[a]=sum%10
                    par=1
                else:
                    num2[a]=sum
                    par=0
            if par==1:
                num2.append(par)
            ans_list=[]
            print(num2)
        for a in num2:
            ans_list.append(ListNode(val=a,next=None)) 
        for a in range(len(ans_list)-1):
            ans_list[a].next=ans_list[a+1]
        return ans_list[0]
        

