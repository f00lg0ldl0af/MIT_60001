# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description) # changed from entry.description to entry.summary
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    """
    Initializes a NewsStory object
            
    guid (string): news story's globally unique identifier
    title (string): news story's headline
    description(string)

    A SubMessage object has five attributes:
        self.message_text (string, determined by input text)
        self.valid_words (list, determined using helper function load_words)
    """
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate
    

        
        


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    """
    Initializes a PhraseTrigger object

    phrase (string): one or more words separated by 
    single space between words, without any punctuations
    
    
    PhraseTrigger returns True when each word in phrase is present
    in its entirety or appears consecutively in text,
    separated only by spaces or punctuation
    """
    def __init__(self, phrase):
        
        assert len(phrase) >= 1, "Type more than one word"
        assert any(p in phrase for p in string.punctuation) == False, "Phrase should not have punctuation"
        if len(phrase.split()) > 1:
            assert phrase.count(" ") >= len(phrase.split()) - 1, "" # should not contain multiple spaces between words
          
        self.phrase = phrase
        Trigger.__init__(self)
    
    def get_phrase(self):
        return self.phrase
        
    def is_phrase_in(self, text):
        for c in text: # format text
            if c in string.punctuation:
                text = text.replace(c," ")
                
        text = text.split()
        text_list = []
        for t_word in text:
            text_list += [t_word.lower()]
        
        phrase_list = [] # format phrase
        phrase = (self.get_phrase()).split()
        for p_word in phrase:
            phrase_list += [p_word.lower()]

        """ ALTERNATIVE
        index_list = []
        for p_word in phrase_list:
            if p_word not in text_list:
                return False
            else:
                for index, t_word in enumerate(text_list):
                    if p_word == t_word:
                        index_list.append(index)
        
        index_val = [index_list[i + 1] - index_list[i] for i in range(len(index_list) - 1)]
        
        for val in index_val:
            if val != 1:
                return False
        return True
        """
        t_index = -1
       
        for j in range(len(text_list)):
            if phrase_list[0] == text_list[j]:
                t_index = j
                break
        
        if t_index == -1 or t_index == (len(text_list)-1):
            return False
        
        else:          
            copy_text = text_list[t_index:t_index + len(phrase_list)]
        
            for i in range(len(phrase_list)):
                if phrase_list[i] == copy_text[i]:
                    continue
                else:
                    return False
            return True 
     
# recursive version of is_phrase_in                    
"""def is_phrase_in_rec(phrase: list[str], text: list[str]):
    # loop over text
    for i in range(len(text)):
        if text[i] == phrase[0]:
            # base case
            if len(phrase) == 1:
                return True 
            # recursive case
            else:
                return is_phrase_in_rec(phrase[1:], text[i+1:])
        else:
            return False"""
    
    
        
# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
        
    def evaluate(self, story):
        return self.is_phrase_in(story.get_title())
        
    
# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):  
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
        
    def evaluate(self, story):
        return self.is_phrase_in(story.get_description())
    
    
# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    """time (string): in EST, in the format of "3 Oct 2016 17:00:10 "."""
    def __init__(self, time):
        time = datetime.strptime(time, "%d %b %Y %H:%M:%S")
        time = time.replace(tzinfo=pytz.timezone("EST"))
        self.triggertime = time
        Trigger.__init__(self)


# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    """Fires alert when story published before trigger time"""
    def __init__(self, time):
        TimeTrigger.__init__(self, time)
    
    def evaluate(self, story):
        return self.triggertime > story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))


class AfterTrigger(TimeTrigger):
    """Fires alert when story published after trigger time"""
    def __init__(self, time):
       TimeTrigger.__init__(self, time)
       
    def evaluate(self, story):
        return self.triggertime < story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))
    


# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    """
    Produces its output by inverting output of another
    trigger.
    
    E.g., if T is TitleTrigger, uses evaluate metehod defined in TitleTrigger
    E.g., if T is BeforeTrigger, uses evaluate method defined in BeforeTrigger
    """
    def __init__(self, T):
        self.T = T
        Trigger.__init__(self)
    
    def evaluate(self, story):
        return not self.T.evaluate(story)
  
    
# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    """
    Fires on a news story only if both of input triggers
    fires on news story item
    """
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2
        Trigger.__init__(self)
    
    def evaluate(self, story):
        return self.T1.evaluate(story) == True and self.T2.evaluate(story) == True
        


# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    """
    Fires on a news story if either one or both of input triggers
    fires on news story item
    """
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2
        Trigger.__init__(self)
    
    def evaluate(self, story):
        return self.T1.evaluate(story) == True or self.T2.evaluate(story) == True



#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)

    story_list = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                story_list.append(story)
                break

    return story_list

    """stories_copy = stories[:]
    for story in stories_copy:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                break
            else:
                stories.remove(story)
    
    return stories"""



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # lines is the list of lines that you need to parse and for which you need
    # to build triggers
    triggers = {}
    triggerlist = []
    
    for line in lines:
        elements = line.split(',')
        if elements[0] == 'ADD':
            for trigger_name in elements[1:]:
                triggerlist.append(triggers[trigger_name])
        else:
            trigger_name = elements[0]
            trigger_type = elements[1]
            
            # add key(trigger_name)-values(trigger rules) into dictionary 
            if trigger_type == 'TITLE':
                triggers[trigger_name] = TitleTrigger(elements[2])

            if trigger_type == 'DESCRIPTION':
                triggers[trigger_name] = DescriptionTrigger(elements[2])

            if trigger_type == 'AFTER':
                triggers[trigger_name] = AfterTrigger(elements[2])
                
            if trigger_type == 'BEFORE':
                triggers[trigger_name] = BeforeTrigger(elements[2])
                
            if trigger_type == 'NOT':
                not_t = triggers[elements[2]] # trigger rule to be NOT'd
                triggers[trigger_name] = NotTrigger(not_t)
            
            if trigger_type == 'OR':
                t1 = triggers[elements[2]]
                t2 = triggers[elements[3]]
                triggers[trigger_name] = OrTrigger(t1, t2)
                
            if trigger_type == 'AND':
                t1 = triggers[elements[2]]
                t2 = triggers[elements[3]]
                triggers[trigger_name] = AndTrigger(t1, t2)

    return triggerlist

    #print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("Hamas")
        t2 = DescriptionTrigger("Israel")
        t3 = DescriptionTrigger("United States")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            #stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

