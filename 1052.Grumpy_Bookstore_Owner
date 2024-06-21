class Solution {
    public int maxSatisfied(int[] customers, int[] grumpy, int X) {
        int sum = 0; 
        
        for(int i = 0; i < customers.length; i++)
        {
            if(grumpy[i] == 0)
            {
                sum+=customers[i];
            }
        }
        
        int satisfaction = sum; 
        int start = 0; 
        int end = start + X - 1;
        int tempSum = 0; 
        
        for(int i = start; i <= end;i++)
        {
            if(grumpy[i] == 1)
            {
                tempSum+= customers[i]; 
            }
        }
        
        int maxWindowSum = tempSum; 
        start++;
        end++;
        while(end < customers.length)
        {
            if(grumpy[start-1] == 1)
            {
                tempSum = tempSum - customers[start-1]; 
            }
            if(grumpy[end] == 1)
            {
                tempSum = tempSum + customers[end];
            }
            
            maxWindowSum = Math.max(tempSum, maxWindowSum);
            start++; 
            end++; 
        }
        
        return (satisfaction + maxWindowSum); 
        
        
        
        //return maxSatONX(customers,grumpy,X);
        //return maxSatONX(customers,grumpy,X);
    }
    
    public int maxSatONPlusX(int[] customers, int[] grumpy, int X)
    {
        int sum = 0; 
        for(int i = 0; i < customers.length; i++)
        {
            if(grumpy[i] == 0)
            {
                sum+=customers[i];
            }
        }
        
        int satisfaction = sum; 
        int start = 0; 
        int end = start + X - 1;
        
        
        
        while(end < customers.length)
        {
            int tempSum = 0; 
            for(int i = start; i<=end;i++)
            {
                if(grumpy[i] == 1)
                {
                    tempSum+= customers[i]; 
                }
                
                satisfaction = Math.max(satisfaction, (sum + tempSum));
            }
            
            start++; 
            end++; 
        } 
        
        return satisfaction;
        
    }
    
    public int maxSatONX(int[] customers, int[] grumpy, int X)
    {
        int row = 0; 
        int satisfaction = Integer.MIN_VALUE; 
        int start = 0; 
        int end = start + X - 1;
        while((end) < customers.length)
        {
            int curSatis = 0; 
            for(int i = 0; i < customers.length; i++)
            {
                if(grumpy[i] == 1 && (i < start || i > end ))
                {
                    continue;
                }
                
                curSatis +=customers[i]; 
            }
            satisfaction = Math.max(curSatis,satisfaction);
            start++; 
            end++; 
        }
 
        return satisfaction; 
    }
}
