
EventIndex = []
Period = []
TimeOfEvent = []
Event = []
TeamResponsible = []
Type = []

RawData = [EventIndex, Period, TimeOfEvent, Event, TeamResponsible, Type]

#Face-Off Arrays
FaceOffWinnerTeam = []
FaceOffLocation = []
FaceOffWinnerNumber= []
FaceOffWinnerName = []
FaceOffLoserNumber= []
FaceOffLoserName = []

#Shot Arrays
ShooterNumber = []
ShooterName = []
ShotType = []
ShotDistance = []

#Stoppage Arrays
StoppageReason = []

#Penalty Arrays
OffenderNumber = []
OffenderName = []
OffenceType = []
PenaltyLength = []

#Goal Arrays
ScorerNumber = []
ScorerName = []
FirstAssistNumber = []
FirstAssistName = []
SecondAssistNumber = []
SecondAssistName = []
GoalShotType = []
GoalShotLength = []

#Plus Arrays
PlusTeam = []
PlusPlayerNumbers = []
PlusPlayerNames = []

#Minus Arrays
MinusTeam = []
MinusPlayerNumbers = []
MinusPlayerNames = []

#Unique Events
UniqueEventList = []




FaceOff = [FaceOffWinnerTeam, FaceOffLocation, FaceOffWinnerNumber, FaceOffWinnerName, FaceOffLoserNumber, FaceOffLoserName]
Shot = [ShooterNumber, ShooterName, ShotType, ShotDistance]
Stoppage = [StoppageReason]
Penalty = [OffenderNumber, OffenderName, OffenceType, PenaltyLength]
Goal = [ScorerNumber, ScorerName, FirstAssistNumber, FirstAssistName, SecondAssistNumber, SecondAssistName, GoalShotType, GoalShotLength]
Plus = [PlusTeam, PlusPlayerNumbers, PlusPlayerNames]
Minus = [MinusTeam, MinusPlayerNumbers, MinusPlayerNames]

nonConstantsInt = [FaceOff, Shot, Stoppage, Penalty, Goal]
nonConstantsTup = [Plus, Minus]


