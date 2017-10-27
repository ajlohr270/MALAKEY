class arxpaper(object):
    """
    Data structure for an Arxiv entry

    ATTRIBUTES
    --------------------------------------------------
    Identifier:     A string identifying the entry
    Date:           A string representing date of submission
    Title:          A string giving the paper title
    Author:         A list of strings giving the authors
    Categories:     A Dictionary containing all the category tags, including
                        -Arxiv (somthing like "math.RT")
                        https://arxiv.org/archive/math
                        -ACM (something like "G.3")
                        http://www.jucs.org/jucs_info/acm_categories
                        -MSC (something like "11J72")
                        http://www.ams.org/mathscinet/msc/msc2010.html
                    keys are the tag, values indicate whether arxiv, ACM, or MSC
    Wordcount:

    (Note: affiliation and keywords are not included yet)
    EXAMPLE
    --------------------------------------------------
    Entry https://arxiv.org/abs/math/0104221v2

    Identifier:     0104221
    Date:           2001-04-25
    Title:          Irrationalite d'au moins un des neuf
                    nombres zeta(5),zeta(7),...,zeta(21)
    Author:         Tanguy Rivoal
    MSC:            {11J72: "MSC_Primary"}
    Wordcount:      ???
    """


    """
    INSTANCE METHODS
    ---------------------------------------------------
    for creating and editing individual entries
    """
    def __init__(self, identifier, date, title, author, category=None, wordcount=None):
        """
        instantiate a paper
        MSC and Wordcount are optional
        """
        self.identifier = identifier
        self.date = date
        self.title = title
        self.author = author
        self.category = category
        self.wordcount = wordcount
 
    def set_wordcount(self, wordcount):
        """
        updates the wordcount dictionary for an entry
        """
        self.wordcount = wordcount


"""
STATIC METHODS
---------------------------------------------------
All of these search through a list and return some
subset of entries matching the search criteria
"""
def search_date(entry_list, date):
    """
    inputs list of entries, returns all that match the date
    """
    L = []
    for arx in entry_list:
        if date == arx.date:
            L.append(arx)
    return L

def search_title(entry_list, title):
    """
    inputs list of entries, returns all that match the title
    """
    L = []
    for arx in entry_list:
        if title == arx.title:
            L.append(arx)
    return L

def search_author(entry_list, author):
    """
    inputs list of entries, returns all that match the author(s)
    """
    L = []
    for arx in entry_list:
        if author == arx.author:
            L.append(arx)
    return L


def search_cat(entry_list, classification):
    """
    inputs list of entries, a classification code
    disregards the type (AMC, MSC or Arxiv)
    returns entries which contain that category
    """
    L = []
    for arx in entry_list:
        if classification in arx.category: 
            L.append(arx)
    return L
            
    
def search_word(entry_list, word):
    """
    inputs list of entries, returns all that have a nonzero
    wordcount for the search word
    """
    L = []
    for arx in entry_list:
        if word in arx.wordcount and arx.wordcount[word]>0:
            L.append(arx)
    return L

        
'''
TESTING
'''

import urllib.request
import feedparser

def class_type(term):
    '''
    takes feedparser category input and returns which
    classification scheme is used
    '''
    if term[0].isdigit():
        return "MSC"
    elif term[1] == ".":
        return "ACM"
    return "Arxiv"

def msc_class(term):
    '''
    inputs feedparser category of MSC type, returns
    dictionary of primary and secondary categories
    '''
    D = {}
    L = term.split()
    if len(L)>1 and L[1] == "(Primary)":
        D[L[0].strip("(),")] = "MSC_primary"
        for n in range(2,len(L)-1):
            D[L[n].strip("(),")] = "MSC_secondary"
    else:
        D[L[0]]= "MSC_primary"
    return D

def stoopid_wordcount(summary):
    '''
    inputs feedparser summary (abstract) and returns
    word frequency dictionary with no filtering of words e.g. "the"
    does filter out some punctuation and html links
    '''
    wordlist = summary.split()
    wordfreq = {}
    for word in wordlist:
        if "http" not in word:
            w = word.strip("(),.:;!?")
            if w not in wordfreq:
                wordfreq[w] = 0
            wordfreq[w] += 1
    return wordfreq
        
faculty = ["Balaban_Tadeusz", "Beals_Robert", "Beck_Jozsef", "Borisov_Lev", "Buch_Anders"]

base_url = 'http://export.arxiv.org/api/query?'
start = 0                    
max_results = 3

ArxData = []

for author in faculty:
    search_query = 'au:'+author
    query = 'search_query=%s&start=%i&max_results=%i' % (search_query, start, max_results)
    response = urllib.request.urlopen(base_url+query).read()
    feed = feedparser.parse(response)
    
    if feed.entries:
        for entry in feed.entries:
            #preprocess abstract
            wc = stoopid_wordcount(entry.summary)

            #preprocess classification
            cat = {}
            for tag in entry.tags:
                classtype = class_type(tag.term)
                if classtype == "MSC":
                    cat.update(msc_class(tag.term))
                else:
                    cat[tag.term] = classtype
            thing = arxpaper(entry.id, entry.date, entry.title, entry.author, cat, wc)
            ArxData.append(thing)

#test wordcount search
for entry in search_word(ArxData, "of"):
    print(entry.title)

#test category search
for entry in search_cat(ArxData, "math.RT"):
    print(entry.title)

for entry in search_cat(ArxData, "math.rt"):
    print(entry.title)
