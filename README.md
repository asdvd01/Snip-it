# Snip-it

ALGORITHM:

The intersection function:
This function receives two sentences, and returns a score for the intersection between them.

We just split each sentence into words/tokens, count how many common tokens we have, and then we normalize the result with the average length of the two sentences.

 f(s1, s2) = |{w | w in s1 and w in s2}| / ((|s1| + |s2|) / 2)


The sentences dictionary:
This part is actually the “Heart” of the algorithm. It receives our text as input, and calculates a score for each sentence. The calculations is composed of two steps:
In the first step we split the text into sentences, and store the intersection value between each two sentences in a matrix (two-dimensional array). So values[0][2] will hold the intersection score between sentence #1 and sentence #3.



Building the summary:
Obviously, the final step of our algorithm is generating the final summary. We do that by splitting our text into paragraphs, and then we choose the best sentence from each paragraph according to our sentences dictionary.


Why this works
There are two main reasons why this algorithm works: 

The first (and obvious) reason is that a paragraph is a logical atomic unit of the text. In simple words – there is probably a very good reason why the author decided to split his text that way. 

The second (and maybe less obvious..) reason is that if two sentences have a good intersection, they probably holds the same information. So if one sentence has a good intersection with many other sentences, it probably holds some information from each one of them- or in other words, this is probably a key sentence in our text!


#Summary
This function receives two sentences, and returns a score for the intersection between them..
In the first step we split the text into sentences, and store the intersection value between each two sentences in a matrix (two-dimensional array).
We do that by splitting our text into paragraphs, and then we choose the best sentence from each paragraph according to our sentences dictionary..
There are two main reasons why this algorithm works:.
The first (and obvious) reason is that a paragraph is a logical atomic unit of the text.
The second (and maybe less obvious..) reason is that if two sentences have a good intersection, they probably holds the same information.

#Usage
1. Complile the summ-it_GUI.py
2. Text box appears, place your text hit
3. Hit summarize to get the summary of the text

#Limitations
1. Doesn't work right for research papers
2. The accuracy rate is 70%

Will be uploading a executable version for windows soon.
