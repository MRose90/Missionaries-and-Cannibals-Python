# Missionaries-and-Cannibals-Python

This is a python script that finds a solution for the missionaries and cannibals problem.

To run the script:
python m&c.py [start] [goal] [search type]
Start and goal are text files that are formatted "[#,#,#,#,#,#]".
	The first # represents the number of missionaries on the left shore.
	The second # represents the number of cannibals on the left shore.
	The fourth # represents the number of missionaries on the right shore.
	The fifth # represents the number of cannibals on the right shore.
	The third and sixth # represents the location of the boat.
Search types:
	bfs
		Breadth first search
	dfs
		Depth first search
	iddfs
		iterative deepening depth first search
	astar
		A* search
The program returns the number of moves required to get the first solution using the search type as well as the number of nodes visited.