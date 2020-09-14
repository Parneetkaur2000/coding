Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

***************************************
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = []
        
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.que.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.que)> 0:
            x = self.que[0]
            self.que.remove(self.que[0])
            return x

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        x = self.que[0]
        return x
        
        

    def empty(self):
        """
        
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.que)>0:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
