
# technical design document

Working on this bc I know how to code a lot better since last working on this. Giving it another go by drafting this TDD before jumping headfirst into the code.

1. Converting the .txt to a json file
(root)
	- pages
		- channel n
			- page n
				- list of timestamped trigger actions
	- patterns
		- 2d array of "order" table. this is what the song is arranged from. each order entry makes up a page on every channel
2. write a function to parse each page into midi instructions
3. make a function to assamble the whole thing into a midi file