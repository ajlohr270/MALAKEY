class arxpaper(object):
    """
    Data structure for an Arxiv entry

    ATTRIBUTES
    --------------------------------------------------
    Identifier:     A string identifying the entry
    Date:           A string representing date of submission
    Title:          A string giving the paper title
    Author:         A list of strings giving the authors
    MSC:            A dictionary containing math subject classifications
                    keys are the subject, value indicates primary or secondary
                    find details about MSC at
                    http://www.ams.org/mathscinet/msc/msc2010.html
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
    MSC:            {11J72: "Primary"}
    Wordcount:      ???
    """


    """
    INSTANCE METHODS
    ---------------------------------------------------
    for creating and editing individual entries
    """
    def __init__(self, identifier, date, author, MSC=None, wordcount=None):
        """
        instantiate a paper
        MSC and Wordcount are optional
        """
 
    def set_wordcount(self, wordcount):
        """
        updates the wordcount dictionary for an entry
        """

    def get_classification(self):
        """
        Looks up the MSC and returns the classification
        Example: if MSC=11J72 then it returns
        "Number Theory: Schmidt Subspace Theorem and applications"
        """

    def get_primary_subject(self):
        """
        Looks up primary MSC and returns subject
        Example: 11J72 returns "Number Theory"
        """



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
    def search_author(entry_list, author):
        """
        inputs list of entries, returns all that match the author(s)
        """
    def search_MSC(entry_list, MSC):
        """
        inputs list of entries, returns all that have a matching
        MSC (either primary or secondary)
        """
    def search_word(entry_list, word):
        """
        inputs list of entries, returns all that have a nonzero
        wordcount for the search word
        """

        
