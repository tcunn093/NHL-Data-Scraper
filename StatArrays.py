
EventIndex = []
Period = []
TimeOfEvent = []
Event = []
TeamResponsible = []
Type = []
Season = []
GameNumber = []

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
PlusPlayerOneNumber = []
PlusPlayerTwoNumber = []
PlusPlayerThreeNumber = []
PlusGoalieNumber = []
PlusPlayerFourNumber = []
PlusPlayerFiveNumber = []
PlusPlayerSixNumber = []
PlusPlayerOneName = []
PlusPlayerTwoName = []
PlusPlayerThreeName = []
PlusGoalieName = []
PlusPlayerFourName = []
PlusPlayerFiveName = []
PlusPlayerSixName = []

#Minus Arrays
MinusTeam = []
MinusPlayerOneNumber = []
MinusPlayerTwoNumber = []
MinusPlayerThreeNumber = []
MinusGoalieNumber = []
MinusPlayerFourNumber = []
MinusPlayerFiveNumber = []
MinusPlayerSixNumber = []
MinusPlayerOneName = []
MinusPlayerTwoName = []
MinusPlayerThreeName = []
MinusGoalieName = []
MinusPlayerFourName = []
MinusPlayerFiveName = []
MinusPlayerSixName = []

#Unique Events
UniqueEventList = []

FaceOff = [FaceOffWinnerTeam, FaceOffLocation, FaceOffWinnerNumber, FaceOffWinnerName, FaceOffLoserNumber, FaceOffLoserName]
Shot = [ShooterNumber, ShooterName, ShotType, ShotDistance]
Stoppage = [StoppageReason]
Penalty = [OffenderNumber, OffenderName, OffenceType, PenaltyLength]
Goal = [ScorerNumber, ScorerName, FirstAssistNumber, FirstAssistName, SecondAssistNumber, SecondAssistName, GoalShotType, GoalShotLength]
Plus = [PlusTeam, 
PlusPlayerOneNumber, 
PlusPlayerTwoNumber, 
PlusPlayerThreeNumber, 
PlusPlayerFourNumber, 
PlusPlayerFiveNumber, 
PlusPlayerSixNumber,
PlusGoalieNumber,
PlusPlayerOneName, 
PlusPlayerTwoName, 
PlusPlayerThreeName, 
PlusPlayerFourName, 
PlusPlayerFiveName, 
PlusPlayerSixName,
PlusGoalieName
]
Minus = [MinusTeam, 
MinusPlayerOneNumber, 
MinusPlayerTwoNumber, 
MinusPlayerThreeNumber, 
MinusPlayerFourNumber, 
MinusPlayerFiveNumber, 
MinusPlayerSixNumber,
MinusGoalieNumber,
MinusPlayerOneName, 
MinusPlayerTwoName, 
MinusPlayerThreeName, 
MinusPlayerFourName, 
MinusPlayerFiveName, 
MinusPlayerSixName,
MinusGoalieName
]

nonConstantsInt = [FaceOff, Shot, Stoppage, Penalty, Goal]
nonConstantsTup = [Plus, Minus]
test = [Season, GameNumber]
Description = nonConstantsInt + nonConstantsTup


