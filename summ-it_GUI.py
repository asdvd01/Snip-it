from __future__ import division
import re

from tkinter import *

  
class SummaryTool(object):
 
    # Naive method for splitting a text into sentences
    def split_content_to_sentences(self, content):
        content = content.replace("\n", ". ")
        return content.split(". ")
 
    # Naive method for splitting a text into paragraphs
    def split_content_to_paragraphs(self, content):
        return content.split("\n\n")
 
    # Caculate the intersection between 2 sentences
    def sentences_intersection(self, sent1, sent2):
 
        # split the sentence into words/tokens
        s1 = set(sent1.split(" "))
        s2 = set(sent2.split(" "))
        #print(s1)
        #print(s2)
        # If there is not intersection, just return 0
        if (len(s1) + len(s2)) == 0:
            return 0
 
        # We normalize the result by the average number of words
        return len(s1.intersection(s2)) / ((len(s1) + len(s2)) / 2)
 
    # Format a sentence - remove all non-alphbetic chars from the sentence
    # We'll use the formatted sentence as a key in our sentences dictionary
    def format_sentence(self, sentence):
        sentence = re.sub(r'\W+', '', sentence)
        return sentence
 
    # Convert the content into a dictionary <K, V>
    # k = The formatted sentence
    # V = The rank of the sentence
    def get_senteces_ranks(self, content):
 
        # Split the content into sentences
        sentences = self.split_content_to_sentences(content)
        #print(sentences)
        # Calculate the intersection of every two sentences
        n = len(sentences)
        #print(n)
        values = [[0 for x in range(n)] for x in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                values[i][j] = self.sentences_intersection(sentences[i], sentences[j])
 
        # Build the sentences dictionary
        # The score of a sentences is the sum of all its intersection
        sentences_dic = {}
        for i in range(0, n):
            score = 0
            for j in range(0, n):
                if i == j:
                    continue
                score += values[i][j]
            sentences_dic[self.format_sentence(sentences[i])] = score
        return sentences_dic
 
    # Return the best sentence in a paragraph
    def get_best_sentence(self, paragraph, sentences_dic):
 
        # Split the paragraph into sentences
        sentences = self.split_content_to_sentences(paragraph)

        # Ignore short paragraphs
        if len(sentences) < 2:
            return ""
 
        # Get the best sentence according to the sentences dictionary
        best_sentence = ""
        max_value = 0
        for s in sentences:
            strip_s = self.format_sentence(s)
            if strip_s:
                if sentences_dic[strip_s] > max_value:
                    max_value = sentences_dic[strip_s]
                    best_sentence = s
 
        return best_sentence
 
    # Build the summary
    def get_summary(self, title, content, sentences_dic):
 
        # Split the content into paragraphs
        paragraphs = self.split_content_to_paragraphs(content)
 
        # Add the title
        summary = []
        summary.append(title.strip())
        summary.append("")
 
        # Add the best sentence from each paragraph
        for p in paragraphs:
            sentence = self.get_best_sentence(p, sentences_dic).strip()
            if sentence:
                summary.append(sentence)
 
        return ("\n").join(summary)
 
 
# Main method, just run "python summary_tool.py"
def main():
    def show_entry_fields():
       content = (e1.get('1.0', END))
          # print(content);
       title = "Summary"
    
##    content = """HELLO THERE, IT'S ME
##
##BABAY LOVE YOU.
##    
##OM IS A BAD BOY."""

       pat = ('(?<!Dr)(?<!Esq)\. +(?=[A-Z])')
       #print (re.sub(pat,'.\n',content))
       # Create a SummaryTool object
       st = SummaryTool()

       # Build the sentences dictionary
       sentences_dic = st.get_senteces_ranks(content)          

       # Build the summary with the sentences dictionary
       summary = st.get_summary(title, content, sentences_dic)

       # Print the summary
       #print(summary)
       root = Tk()
       T = Text(root, height=50, width=120)
       T.pack()
       T.insert(END, summary)
#       T.insert(END,".")

       # Print the ratio between the summary length and the original length
       print (" ")
       print ("Original Length %s" % (len(title) + len(content)))
       print ("Summary Length %s" % len(summary))
       print ("Summary Ratio: %s" % (100 - (100 * (len(summary) / (len(title) + len(content))))))

    def clear():
       e1.delete('1.0', END)
    def quit():
       exit(0)


          
      
    master = Tk()
    Label(master, text="Enter Text").grid(row=0, column=0)
    master.config(height=370, width=670)
    e1 = Text(master, width=50, height=10, exportselection=0,padx=100, pady=100)
    e1.grid(row=2, column=0)
    scrl = Scrollbar(master, command=e1.yview)
    e1.config(yscrollcommand=scrl.set)
    scrl.grid(row=2, column=3, sticky='ns')
    Button(master, text='Quit', command=quit).grid(row=4, column=0, sticky=W, pady=4)
    Button(master, text='Summarize', command=show_entry_fields).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Clear', command=clear).grid(row=5, column=0, sticky=W, pady=4)


   
 
    # Demo
    # Content from: "http://thenextweb.com/apps/2013/03/21/swayy-discover-curate-content/"
 
  
 
 
if __name__ == '__main__':
    main()
