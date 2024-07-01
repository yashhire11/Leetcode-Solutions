//2:23
//Problem
//Markdown
//Visualize
//Code + Unit Tests
//Complexity
//MARK : Unit Tests



//Mark: Solution
class Solution {
    var result = ""
    ///Func to minimum length crack
    ///Parameters:
    ///. - n : Int, 1<= n <=4
    ///  - k : Int, 1<= k <=10
    ///
    /// minimum length that will unlock the safe at some point
    ///
    ///Approch DFS + Backtracking
    ///time Complexity :
    ///. Space Complexity :
    ///. - Returns : String , Return any string of minimum length that will unlock the safe at some point of entering it.
    func crackSafe(_ n: Int, _ k: Int) -> String {

        //base case
        if n==1 && k==1 {
            return "0"
        }

        //Memoize
        var visited = Set<String>()
        var start = String(repeating: "0", count: n-1)
        dfs(start, k , &visited)
        result.append(start)
        return result
    }

    func dfs(_ start: String, _ k: Int, _ visited: inout Set<String>){
        for index in 0..<k{
            var neighbor = "\(start)\(index)"
            if !visited.contains(neighbor) {
                visited.insert(neighbor)
                var charArray = [Character](neighbor)
                dfs(String(charArray[1...]), k , &visited)
                result.append(String(index))
            }
        }
    }
}

extension StringProtocol{
    subscript(index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}

//Input: n = 1, k = 2
//Output: "10"

//1 "1"
//0 "10"

//Input: n = 2, k = 2
//Output: "01100"

//00 ('00' 110)
// 01 (0 '01' 10)
//  11 (00 '11' 0)
//   10 (001 '10')


//.        00
//.       01 10
