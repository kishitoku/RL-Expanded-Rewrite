# Base Actor Class (and examples?)
#
# Actors will be anything (usually a character/person) the player can interact with
# 
# Example Group
#   Example Sub-Group 
#       Written Name (variableName) (type) (other info)
#
# Actors contain:
#   Actor Information (N/A) (N/A)
#       Actor Name (actorName) (string)
#       Default Name (name) (string)
#       Pet Name (petName) (string)
#       Pet Names (petNames) (set)
#       Dialog Color (dialogColor) (string) (name of supported color or hex #)
#   Actor Stats (actorStats) (dictionary) (relative to player)
#       Addiction (addiction) (integer) (0-100)
#       Addiction Rate  (addRate)  (integer) (0-10)
#       Addiction Resistance (addResist)  (integer) (0-3)
#       Inhibition (inhbt)  (integer) (1000-0)
#       Love (love)  (integer) (0-1000)
#       Lust (lust)  (integer) (0-100)
#       Obedience (obed)  (integer) (0-1000)
#   Other Statistics (N/A) (N/A)
#       Actions (?) TODO: Get more info on how actions work
#       Sexual interactions (N/A) (N/A) (pretty self-explanatory)
#       Dialog interactions (N/A) (N/A) (ex: # of times player spoke w/ them not including intro scenes etc)
#       Any other types of interactions (N/A) (N/A) (tbd/wip stuff)
#   Wardrobe Information (N/A) (N/A)
#       Current Layer Settings (N/A) (N/A)
#
# Actors handle:
#   Updates for
#       - Actor Info.
#       - Actor Stats
#       - Interaction Stats
#
# NOTE: Actors do not handle wardrobe changes!

init -2 python:
    import re

    class Actor(renpy.store.object):
        """docstring for Actor"""
        def __init__(self, actorName, name, **kwargs):
            # Actor Information
            self.actorName = actorName  # Programmers needs come first :P
            self.name = name
            self.petNames = kwargs.get('names',[self.name,'Nickname','Pet-Name'])
            # self.petName = petNames[0]
            self.dialogColor = kwargs.get('dialogColor',"#000000")

            # self.actions = #???

            # Actor Stats (relative to the player)
            self.actorStats = kwargs.get('actorStats',{
                                            'level':0,'xp':0,'sexExp':0,
                                            'maxActions':3,'actions':3, # max actions during sex & counter of # of avaliable actions
                                            'addiction':0,'addRate':0,'addResist':0,
                                            'inhbt':1000,'love':0,'lust':0,'obed':0})

            # Sexual Stats (relative to player and other actors) (may need to rename some variables here when actions are implemented)

            self.actorSeen = kwargs.get('actorSeen',{
                                            'playerUnderwear':0,'playerBody':0,'playerChest':0,'playerGenitals':0,'lezSex':0}) 
                                            # Player and others exposed what to this Actor?

            self.actorExposed = kwargs.get('actorExposed',{
                                            'exposedUnderwear':0,'exposedBody':0,'exposedChest':0,'exposedGenitals':0,'exposedLezSex':0,}) 
                                            # This Actor exposed what to Player? (/seen doing what by Player?)
            # TODO: move sex acts to object base?
            self.actorSexActs = kwargs.get('actorActs',{
                                            'actMassaged':0,'actKissed':0,'actStripped':0,'actSlept':0, # slept with player (not sex)
                                            'actFondleChest':0,'actFondleButt':0,'actSlapButt':0,
                                            'actFondleAnus':0,'actFondleGenitals':0, 
                                            'actLickChest':0,'actLickAnus':0,'actLickGenitals':0,
                                            'actHandjob':0,'actTitjob':0,'actBlowjob':0,'actFootjob':0,
                                            'actHotdog':0,'actMasturbate':0,'actAnal':0,'actVaginal':0,
                                            'actInsertAnus':0,'actInsertVaginal':0,
                                            'actDildoAnus':0,'actDildoVagina':0,'actVibrator':0,'actButtplug':0,
                                            'actCreampieSwallow':0,'actCreampieAnus':0,'actCreampieVagina':0,
                                            'actOrgasms':0,
                                            'actEncounterOrgasams':0,'actCaught':0})
                                            # This Actor has done what with Player? (/Player has done to Actor)
            # A dictionary serving to hold active emotions and other things of note, this is a hold-over from the og game and needs to be replaced!
            self.actorStatus = kwargs.get('actorStatus',{'normal':0})

