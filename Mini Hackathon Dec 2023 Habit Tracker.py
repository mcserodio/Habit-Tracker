#create a class for each user to keep track of their info
#within this class should be an empty dictionary which we can append
#   values to
import datetime

class User:
    def __init__(self,username):
        self.name=username
        self.stats={} #(KEY) day # : (VALUE) [STR, DEF, WSD, SPD], level
        self.level=1 #all users start at level 1
        self.prog_left=0 #what % of progress bar needed 'til next level-up
    def level_up(self,progress_bar): #input % of progress, e.g. 140
        if progress_bar>=100:
            self.level+=(progress_bar//100) #adds int, not float
        #(can only have whole levels, not portions)
            self.prog_left=(100-(progress_bar%100))
    def add_stats(self,day,_str,_def,_wsd,_spd):
        self.stats[day]=[_str,_def,_wsd,_spd]
    def update_str(self,day,_str): 
            self.stats[day][0][0]=_str #changes first index (0) of DAY key's list value
    def update_def(self,day,_def):
        self.stats[day][0][1]=_def
    def update_wsd(self,day,_wsd):
        self.stats[day][0][2]=_wsd
    def update_spd(self,day,_spd):
        self.stats[day][0][3]=_spd


#loop to have user log in; if no users exist yet, they must create one


print("Welcome to your progress tracker!")
username=input("What is your username? ")
user=User(username)
print("Hi,",user.name+"!")

#another loop for what they want to do
end=False
while end==False:
    action=input("What would you like to do? Update (l)evel, (a)dd today's \
stats,(m)odify past stats, or view progress (r)eport? ")
    if action=='l':
        progress_bar=input("How much level progress did you make today? (Enter a percentage value) ")
        user.level_up(progress_bar)
        print('You have',user.prog_left,'progress percentage left to level up!')
    elif action=='a': #data validation who?
        print("You are making an entry for",datetime.date.today())
        day=datetime.date.today()
        _str=input("How many STR points did you gain? ")
        _def=input("How many DEF points did you gain? ")
        _wsd=input("How many WSD points did you gain? ")
        _spd=input("How many SPD points did you gain? ")
        level=input("What is your current level? ")
        user.stats[str(day)]=[_str,_def,_wsd,_spd],level
    elif action=='m':
        valid_day=False
        while valid_day==False:
            day=input("Which day's stats would you like to modify? (YYYY-MM-DD) ")
            if day in user.stats:
                valid_day=True
            else:
                print("Invalid input.",day+"'s entry does not exist.")
        #may need to validate ^^ that it's a number 
        choose_stat=input("Which stat would you like to modify? (STR, DEF, WSD, SPD) ")
        if choose_stat=='STR':
            _str=input("How many STR points did you gain? ")
            user.update_str(day,_str)
        elif choose_stat=='DEF':
            _def=input("How many DEF points did you gain? ")
            user.update_def(day,_def)
        elif choose_stat=='WSD':
            _wsd=input("How many WSD points did you gain? ")
            user.update_wsd(day,_wsd)
        elif choose_stat=='SPD':
            _spd=input("How many SPD points did you gain? ")
            user.update_spd(day,_spd)
        else:
            print("Invalid input.")

    elif action=='r':
        if user.stats=={}:
            print("No data has been entered yet.")
        else:
            for key,item in user.stats.items():
                print("On day",key,'your stats were: STR',user.stats[key][0][0],',DEF',user.stats[key][0][1],'WSD'\
                      ,user.stats[key][0][2],'SPD',user.stats[key][0][3])
    else:
        ("Invalid input.")
