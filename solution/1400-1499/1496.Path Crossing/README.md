# [1496. 判断路径是否相交](https://leetcode-cn.com/problems/path-crossing)

[English Version](/solution/1400-1499/1496.Path%20Crossing/README_EN.md)

## 题目描述

<!-- 这里写题目描述 -->

<p>给你一个字符串 <code>path</code>，其中 <code>path[i]</code> 的值可以是 <code>&#39;N&#39;</code>、<code>&#39;S&#39;</code>、<code>&#39;E&#39;</code> 或者 <code>&#39;W&#39;</code>，分别表示向北、向南、向东、向西移动一个单位。</p>

<p>机器人从二维平面上的原点 <code>(0, 0)</code> 处开始出发，按 <code>path</code> 所指示的路径行走。</p>

<p>如果路径在任何位置上出现相交的情况，也就是走到之前已经走过的位置，请返回 <code>True</code> ；否则，返回 <code>False</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://cdn.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1496.Path%20Crossing/images/screen-shot-2020-06-10-at-123929-pm.png" style="height: 224px; width: 250px;"></p>

<pre><strong>输入：</strong>path = &quot;NES&quot;
<strong>输出：</strong>false 
<strong>解释：</strong>该路径没有在任何位置相交。</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://cdn.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1496.Path%20Crossing/images/screen-shot-2020-06-10-at-123843-pm.png" style="height: 212px; width: 250px;"></p>

<pre><strong>输入：</strong>path = &quot;NESWW&quot;
<strong>输出：</strong>true
<strong>解释：</strong>该路径经过原点两次。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= path.length &lt;= 10^4</code></li>
	<li><code>path</code> 仅由 <code>{&#39;N&#39;, &#39;S&#39;, &#39;E&#39;, &#39;W}</code> 中的字符组成</li>
</ul>

## 解法

<!-- 这里可写通用的实现逻辑 -->

<!-- tabs:start -->

### **Python3**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```python
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        vis = set([(x, y)])
        for c in path:
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x += 1
            else:
                x -= 1
            if (x, y) in vis:
                return True
            vis.add((x, y))
        return False
```

### **Java**

<!-- 这里可写当前语言的特殊实现逻辑 -->

```java
class Solution {
    public boolean isPathCrossing(String path) {
        int x = 0;
        int y = 0;
        Set<Integer> vis = new HashSet<>();
        vis.add(0);
        for (char c : path.toCharArray()) {
            if (c == 'N') {
                ++y;
            } else if (c == 'S') {
                --y;
            } else if (c == 'E') {
                ++x;
            } else {
                --x;
            }
            int t = x * 20000 + y;
            if (vis.contains(t)) {
                return true;
            }
            vis.add(t);
        }
        return false;
    }
}
```

### **C++**

```cpp
class Solution {
public:
    bool isPathCrossing(string path) {
        int x = 0, y = 0;
        unordered_set<int> vis{{0}};
        for (char c : path)
        {
            if (c == 'N') ++y;
            else if (c == 'S') --y;
            else if (c == 'E') ++x;
            else --x;
            int t = x * 20000 + y;
            if (vis.count(t)) return 1;
            vis.insert(t);
        }
        return 0;
    }
};
```

### **Go**

```go
func isPathCrossing(path string) bool {
	x, y := 0, 0
	vis := make(map[int]bool)
	vis[0] = true
	for _, c := range path {
		if c == 'N' {
			y++
		} else if c == 'S' {
			y--
		} else if c == 'E' {
			x++
		} else {
			x--
		}
		t := x*20000 + y
		if vis[t] {
			return true
		}
		vis[t] = true
	}
	return false
}
```

### **...**

```

```

<!-- tabs:end -->
