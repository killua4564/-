# Main
* You should edit in sif.py

# Member object
* Member([name], [score], [hole], [add_score], [center_skill])
	* name = [rarity]\_[last_name]
	* add_score = add_score_compute([condition], [note], [percentage], [score]) or 0
		* condition = (note, combo, perfect, second)	
			* ex: For every 22 notes, there is a 29% chance of increasing players score by 700 points.
			* ==> add_score_compute('note', 22, 0.29, 700)
	* center_skill = (Grade, Team, Unit)
		* ex: Smile point up 9%, and BiBi member smile up 6%
		* ==> 'Unit'
		* There's no double attributes center skill choice

# Team object
* Team([name], [Member object list])
	* Length of Member object list must be 9

# perfect_rate
* You can evaluate your perfect rate in this. It'll let your score higher because of yourself.

# Version
* 2.2 add personal +1400 and team 4%
* 2.1 fix add_score problem
* 2.0 add decide center system, after fill the hold
* 1.6 function add_score_compute condition add second
* 1.5 improve efficiency
* 1.3 fix some problems
* 1.2 add average score
* 1.0 original version# LoveLive-School-idol-festival
