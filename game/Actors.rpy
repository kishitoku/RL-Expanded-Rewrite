init -1 python:

    import renpy

    class Sex(object):
        def __init__(self, actions = 3):
            super(Sex, self).__init__()
            self.actions = actions

        def addCount(self, action, count):
            self.sexCounts[action] += count

        def addSeen(self, part, count):
            self.seen[part] += count

        def getCount(self, action):
            return self.sexCounts[action]

        def getSeen(self, part):
            return self.seen[part]

        # Seen counts.
        self.seen = {
            'bra': 0,
            'chest': 0,
            'panties': 0,
            'penis': 0,
            'pussy': 0
            }

        # Sex history. Why is so much recorded? Trim if possible.
        # Lets move sexCounts to some sort of stats holder.
        self.sexCounts = {
            'anal': 0,
            'assSlapped': 0,
            'blowjob': 0,
            'caught': 0,
            'creamedAss': 0,
            'creamedPussy': 0,
            'dildoAss': 0,
            'dildoPussy': 0,
            'fondledA': 0,
            'fondledB': 0,
            'fondledP': 0,
            'fondledT': 0,
            'footRub': 0,
            'handHold': 0,
            'hotdogged': 0,
            'kissed': 0,
            'lesbian': 0,
            'lesWatch': 0,
            'lickedAss': 0,
            'lickedPenis'; 0,
            'massaged': 0,
            'masturbated': 0,
            'orgasmed': 0,
            'sleepOver': 0,
            'stripped': 0,
            'swallowed': 0,
            'usedVibe': 0,
            'usedPlug': 0
            }

    class Player(ADVCharacter):
        def __init__(self, name = "Zero", color = "green", **kwargs):
            # default player name is Zero
            self.name = name
            # Color can currently be green, white, or black. May need checker.
            self.color = color
            # Set level of the player to 1. May add func to calc level.
            self.level = 1
            # Set current xp to 0
            self.xp = 0
            # Inventory is a simple list.
            self.inventory[]
            # Money is stored as a separate value. Default start of $0
            self.cash = 0
            # Set an initial income value.
            self.income = 10

        def copy

    class Girl(ADVCharacter):
        def __init__(
                self,
                name,
                inbt = 1000,
                love = 0,
                lust = 0,
                obed = 0,
                actions,
                addiction
                addictionRate = 0,
                addictionResist = 0,
                ):
            # Basic information:
            self.name = name
            self.inbt = inbt
            self.love = love
            self.lust = lust
            self.obed = obed
            self.xp = 0
            self.level = 0
            self.addiction = addiction
            self.addictionRate = addictionRate
            self.addictionResist = addictionResist

            self.sex = Sex(actions)
