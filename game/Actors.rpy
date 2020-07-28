init -1 python:

    import renpy

    class Sex(object):
        def __init__(self, actions = 3):
            super(Sex, self).__init__()
            self._actions = actions

        def addCount(self, action, count):
            self._sexCounts[action] += count

        def addSeen(self, part, count):
            self._seen[part] += count

        def getCount(self, action):
            return self._sexCounts[action]

        def getSeen(self, part):
            return self._seen[part]

        # Seen counts.
        self._seen = {
            'bra': 0,
            'chest': 0,
            'panties': 0,
            'penis': 0,
            'pussy': 0
            }

        # Sex history. Why is so much recorded? Trim if possible.
        # Lets move sexCounts to some sort of stats holder.
        self._sexCounts = {
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
            self._name = name
            # Color can currently be green, white, or black. May need checker.
            self._color = color
            # Set level of the player to 1. May add func to calc level.
            self._level = 1
            # Set current xp to 0
            self._xp = 0
            # Inventory is a simple list.
            self._inventory[]
            # Money is stored as a separate value. Default start of $0
            self._cash = 0
            # Set an initial income value.
            self._income = 10

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
            self._name = name
            self._inbt = inbt
            self._love = love
            self._lust = lust
            self._obed = obed
            self._xp = 0
            self._level = 0
            self._addiction = addiction
            self._addictionRate = addictionRate
            self._addictionResist = addictionResist

            self._sex = Sex(actions)
