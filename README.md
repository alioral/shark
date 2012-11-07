<h2>Shark</h2>

<p>Shark is a web crawler that helps you *possibly* 
find great coders using the Github Network. </p>

<p><h3>Idea</h3> Since nowadays every tech company from startups to huge corporations, 
take Github into consideration and would like to hire best hackers, 
Shark helps them out by relying on some of the facts I've pre-defined.
It all starts by the user choosing a company. 
The reason is for that we would *again, possibly* 
trust the endorsements(in this case endorsements are being followed by the company member) 
of engineers from companies such as Facebook, Twitter etc. 
So the crawler basic brings you the Github profiles that are 
possibly great hackers by taking connections in consideration.
(Note from the Author: Of course, # of repos, starts were some of the
conditions I could take into consideration, but hey, what is better
than being followed by a talented engineer?)
</p>

<p>
	<h3>Parameters:</h3>
	<code>shark.py <github_company_url> <depth> <num_of_hackers></code>
</p>
<p>
	<h3>Example: </h3>
	<code>python shark.py https://github.com/joyent 2</code>
</p>
<p>
	<h3>Algorithm:</h3>
	
	<ol>
		<li>For given company URL, retrieve all the members</li>
		<li>For each member, find the people who are followed by that 
		member and insert them into a hashtable with rank.</li>
		<li>If a particular person shows up again increment its rank.</li>
		<li>When all the members' followings scanned, sort the hashtable according to rank, 
		bring the top N developers from the hashtable.</li>
	</ol>
</p>
<p>If the depth is defined, the crawler will look for the friends of friends of the member and etc. 
(Depth is defined, in order to prevent the infamous "Six Degrees of Kevin Bacon"</p>