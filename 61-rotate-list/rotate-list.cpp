/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next || k == 0) return head;
        int l=1;
        ListNode* temp=head;
        while(temp->next)
        {
            temp=temp->next;
            l++;
        }
        temp->next=head;
        k=k%l;
        int steps=l-k;
        temp=head;
        for(int i=0;i<steps-1;i++)
        {
            temp=temp->next;

        }
        head=temp->next;
        temp->next=NULL;
        return head;
    }
};