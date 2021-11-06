# Election_Analysis

## Project Overview
While parterning with the Colorado Board of Elections, we were given the following tasks to complete in order to audit the results of a recent congressional election. We were asked to determine:

1. Total number of votes cast for the election
2. A complete list of candidates who received votes
3. Total number of votes cast in each county
4. Percentage of votes cast in each county
5. Total number of votes each candidate received
6. Percentage of votes each candidate won
7. The winner of the election based on popular vote

## Resources
- Data Source: election_results.csv
- Software: Python 3.10.0, Visual Studio Code 1.62.0

## Summary
The analysis of the election data showed that:
- There were 369,711 total votes cast in the election.
- The votes cast per county were:
    - Jefferson county voters cast 38,855 votes - 10.5% of the total.
    - Denver county voters cast 306,055 votes - 82.8% of the total.
    - Arapahoe county voters cast 24,801 votes - 6.7% of the total.
- The county with the largest number of votes was:
    - Denver county, with 82.8% of the vote and 306,055 total votes.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 total votes.
    - Diana DeGette received 73.8% of the vote and 272,892 total votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 total votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 total votes.

## Challenge Analysis Overview
We used Python code to evaluate the election data supplied in a csv file, tabulate the election results, and print those results to a text file to supply to the Board of Elections. The election results were determined through the following steps:
1) In the first section we declared string, integer, list and dictionary variables needed to analyze and track the elecation data:
![Declare Variables](https://github.com/jmueller187/Election_Analysis/blob/main/Resources/PyPollChallengeDeclareVariables.png)

2) The next section was used to write **for** and **if** loops to determine total number of election votes, votes cast for each candidate and votes cast in each county:
![Summarize total votes, votes per candidate and votes per county](https://github.com/jmueller187/Election_Analysis/blob/main/Resources/PyPollChallengeVoteTally.png)

3) Once totals were determined and saved to our lists and dictionaries, we were able to open our text file and print our results, starting with total votes, votes per county and largest county turnout:
![Summary of total votes, county votes and largest county turnout](https://github.com/jmueller187/Election_Analysis/blob/main/Resources/PyPollChallengePrintTotalVotesWinningCounty.png)

And ending with candidate summary and the winning candidate:
![Summary of candidate votes and winning candidate](https://github.com/jmueller187/Election_Analysis/blob/main/Resources/PyPollChallengePrintWinningCandidate.png)

## Challenge Summary
In summary, Python allowed so to audit and summarize the votes cast in three counties for three candidates, and determine the winning candidate, largest county turnourt and total votes cast. In addition to this election, the script could also be used - with some additional modifications - to audit the results for any election. For example, we could modify the script for a state-wide governor race, and breakout results to determin votes in each city in the state, vottes per candidate and the winning candidate. We could also modify the script for a city's mayoral race and breakout results to determine votes in each city voting district along with the candiates receiving votes and the winning candidate.

