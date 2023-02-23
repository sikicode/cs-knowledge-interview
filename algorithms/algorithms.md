1. Iteration vs Recursion (e.g. binary search)
<br>Recursion solves the problem by function itself, feed the result back into function.
<br>While Iteration use loops to repeat a set of instructions
<br><mark>Recursion is usually slower than iteration due to the overhead of maintaining the stack. Recursion uses more 
memory than iteration. Recursion makes the code smaller.</mark>

2. Dynamic Programming 
- Why DP performs better than recursion with memo?
 <br>Ans: DP does not need extra space to store computed results from recursion.
Reference Leetcode 4: https://wy-ei.github.io/leetcode/dp/

3. Deterministic Finite Automation (DFA State Machines)
- Def: A state machine reads some input and changes the states based on those inputs. state machines with a finite 
number of states are called finite state machines. (state machine + transition)
- Regex Matching Syntax: https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html
- Construct NFA and turn NFA to DFA: 
- Sample Design: <br><img src="./img/state machine example.png" width="900"/> <br>Check initial state,
  accepting state and dead state
- Questions: [8](https://leetcode.com/problems/string-to-integer-atoi/description/),
             [65](https://leetcode.com/problems/valid-number/),
             [10](https://leetcode.com/problems/regular-expression-matching/),
             [44](https://leetcode.com/problems/wildcard-matching/),
             [520](https://leetcode.com/problems/detect-capital/),
             [890](https://leetcode.com/problems/find-and-replace-pattern/),
             [1018](https://leetcode.com/problems/binary-prefix-divisible-by-5/)

4. Reverse Number Questions (palindrome, reversing): To speed up, use log(n) to the base 10 which means to divide 10 
and handle. Notice 32 bit boundaries to avoid overflow/underflow. char.isdigit() can be useful.

5. 
