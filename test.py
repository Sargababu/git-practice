import csv
import json


class TestClass(object):

    def __init__(self, foo, bar, baz):
        self.foo = foo
        self.bar = bar
        self.baz = baz

    def fizz_buzz(self, digit_1, digit_2):
        for i in range(1, 100):
            if i % digit_1 == 0:
                if i % digit_2 == 0:
                    print 'fizzbuzz!'
                else:
                    print 'fizz!'
            elif i % digit_2 == 0:
                print 'buzz!'
            else:
                print i
    def get_randword():
        """This function helps in getting random word from the file"""
        with open('/home/sarga/text_words.txt','r') as f:
            rword = f.read().split(" ")
        return random.choice(rword)
    
    def read_lettr(my_word,g_word, trials):    
        g_lettr = raw_input("Enter your guess: ")
        out = map(lambda x,y:y if y else "*",my_word, g_word)
        print ''.join(out)
        trials = check_word(my_word,g_word,g_lettr,trials)
        if trials==0 :
            print"SORRY, YOU LOSE"
            res = raw_input("Play Again?? type yes or else press any key ")
            if res.lower() == "yes":
                game()
            else:
                exit(0)
        read_lettr(my_word,g_word,trials)
    

    def json_to_csv(self, json_file_path, outfile_path):
        """Convert a file containing a list of flat JSON objects to a csv.

        What's a DictWriter, you say? Never heard of it!

        """
        with open(json_file_path) as f:
            data = json.load(f)
        with open(outfile_path, 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(data[0].keys())
            for item in data:
                writer.writerow(item.values())
