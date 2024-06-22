class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null || head.next==null){
            return head;
        }

        ListNode curr = head;
        int length = 1;

        while(curr.next!=null){
            length++;
            curr = curr.next;
        }

        curr.next = head;
        k = k%length;
        k = length -k;

        while(k-->0){
            curr = curr.next;
        }

        head = curr.next;
        curr.next = null;
        return head;
    }
}
