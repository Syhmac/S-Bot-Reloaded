## -- Generic terms --
genericMember = "member"
genericReason = "reason"
## -- Error messages --
errorNoPermission = "You don't have permission to use this command."
errorForbidden = "I don't have permission to perform this action."
errorUnexpected = "An unexpected error occurred while executing the command."
errorCooldown = "This command is on cooldown. Please try again in {time}s."
## -- Utility commands --
# ping
pingCommandName = "ping"
pingCommandDescription = "Check the bot's latency"
pingCommandResponse = "Pong! Bot's latency is {latency} ms."
## -- Economy commands --
# balance
balanceCommandName = "balance"
balanceCommandDescription = "Check your current balance"
balanceCommandResponse = "Your current balance is {balance} :coin:."
# job
jobCommandName = "job"
jobCommandDescription = "Work a job to earn some coins"
jobList = {
    1: "{user} worked at McDonald's restaurant and earned {earnings} :coin:.",
    2: "{user} worked at Walmart and got {earnings} :coin: for it.",
    3: "{user} worked as a barista at a local coffee shop and earned {earnings} :coin:. They also got {tips} :coin: in tips!",
    4: "{user} worked at Uber Eats and earned {earnings} :coin: for delivering food. They also got a {tips} :coin: tip for being fast!",
    5: "{user} took a freelance programming gig and earned {earnings} :coin: for it.",
    6: "{user} worked as a ticket inspector and earned {earnings} :coin: for catching fare dodgers.",
    7: "{user} mowed a lawn in the neighborhood and earned {earnings} :coin: with additional {tips} :coin: in tips for doing a great job!",
    8: "{user} walked a dog for an hour and earned {earnings} :coin: for it. The dog's owner gave them {tips} :coin: tip for keeping the dog happy!",
    9: "{user} endured a stressful day of babysitting and earned {earnings} :coin: for it. They also got {tips} :coin: in tips for keeping the kids entertained!",
    10: "{user} cleaned someone's house and earned {earnings} :coin: for it. They also got {tips} :coin: in tips for dusting high shelves!",
    11: "{user} washed a car and earned {earnings} :coin: for it. They also got {tips} :coin: in tips for making the car shine!",
    12: "{user} fixed a computer and earned {earnings} :coin: for it.",
    13: "{user} tutored a student and earned {earnings} :coin: for it. They also got {tips} :coin: in tips after the student passed the test with A!",
    14: "{user} worked an office job and earned {earnings} :coin: for it.",
    15: "{user} worked as a bartender and earned {earnings} :coin: with {tips} :coin: in tips for making great cocktails!",
    16: "{user} worked as a waiter and earned {earnings} :coin: with {tips} :coin: in tips for providing excellent service!",
    17: "{user} worked as a security guard and earned {earnings} :coin: for it.",
    18: "{user} helped organize an event and earned {earnings} :coin: for it.",
    19: "{user} worked as a garbage collector. It was a dirty job, but {user} earned {earnings} :coin: for it.",
    20: "{user} helped translate an important document and got paid {earnings} :coin: for it.",
    21: "{user} worked as Uber driver and earned {earnings} :coin: for it. They also got {tips} :coin: in tips for providing a smooth ride!",
    22: "{user} worked at 7-11 and earned {earnings} :coin: for it.",
    23: "{user} took an art commission and earned {earnings} :coin: for it.",
    24: "{user} wrote a blog post and earned {earnings} :coin: for it.",
    25: "{user} worked at a call center and earned {earnings} :coin: for it.",
    26: "{user} did some gardening work and earned {earnings} :coin: for it. They also got {tips} :coin: in tips for making the flowers look better than ever!",
    27: "{user} printed a 3D model for a client and earned {earnings} :coin: for it.",
    28: "{user} did a photoshoot and earned {earnings} :coin: for it.",
    29: "{user} worked as a chef at the restaurant and earned {earnings} :coin: for it.",
    30: "{user} made a YouTube video and earned {earnings} :coin: from ad revenue.",
    31: "{user} did a livestream on Twitch and earned {earnings} :coin: from donations and subscriptions.",
    32: "{user} worked as a police officer and earned {earnings} :coin: for writing enough parking tickets.",
    33: "{user} worked as a firefighter and earned {earnings} :coin: for extinguishing a fire.",
    34: "{user} worked as a paramedic and earned {earnings} :coin: for saving a life.",
    35: "{user} worked as a teacher and earned {earnings} :coin: for it.",
    36: "{user} worked as a bus driver and earned {earnings} :coin: for it.",
    37: "{user} worked as a train conductor and earned {earnings} :coin: for it.",
    38: "{user} worked as a train driver and earned {earnings} :coin: for it.",
    39: "{user} worked as a pilot and earned {earnings} :coin: for it.",
    40: "{user} flew to space as an astronaut and got paid {earnings} :coin:.",
    41: "{user} worked as a tram driver and earned {earnings} :coin: for it.",
    42: "{user} bought some products from AliExpress and resold them on Amazon for a profit, earning {earnings} :coin:.",
    43: "{user} worked as a veterinarian and earned {earnings} :coin: for treating sick animals.",
    44: "{user} volunteered at an animal shelter. They didn't get paid, but at least they helped some cute animals!",
    45: "{user} delivered fresh vegetables as a truck driver and earned {earnings} :coin: for it.",
    46: "{user} joined a few cables and fixed the electricity in a house, earning {earnings} :coin: for it.",
    47: "{user} fixed a leaky pipe and earned {earnings} :coin: for it.",
    48: "{user} built a nice coffee table and earned {earnings} :coin: for it.",
    49: "{user} went door-to-door selling vacuum cleaners and earned {earnings} :coin: for it.",
    50: "{user} took their guitar on the street and played some music, earning {earnings} :coin: in donations from passersby.",
    51: "{user} harvested some crops on their farm and sold them on the local market for {earnings} :coin:.",
    52: "{user} made a handmade bracelet and sold it online for {earnings} :coin:.",
    53: "{user} rented out their car for {earnings} :coin:.",
    54: "{user} helped someone move to a new house and earned {earnings} :coin: for it.",
    55: "{user} participated in beta testing of a new app and earned {earnings} :coin: for providing feedback and reporting bugs.",
    56: "{user} took a few paid online surveys and earned {earnings} :coin: for sharing their opinions.",
    57: "{user} worked as a zookeeper and earned {earnings} :coin: for taking care of the animals.",
    58: "{user} worked as a museum guide and earned {earnings} :coin: for it.",
    59: "{user} made a fandub of a popular movie and earned {earnings} :coin: from ad revenue and sponsorships.",
    60: "{user} did some voice acting for a commercial and earned {earnings} :coin: for it.",
    61: "{user} worked at a hot dog stand and earned {earnings} :coin: for it.",
    62: "{user} drove and ice cream truck around the neighborhood and earned {earnings} :coin: for it.",
    63: "{user} worked as a hotel receptionist and earned {earnings} :coin: for it.",
    64: "{user} worked as a pool lifeguard and earned {earnings} :coin: for it.",
    65: "{user} worked as a personal maid and earned {earnings} :coin: for it. Yes, they had to wear a maid outfit while doing it.",
}
## -- Administrative commands --
# kick
kickCommandName = "kick"
kickCommandDescription = "Kicks user from the server"
kickCommandMemberDescription = "Member to kick"
kickCommandReasonDescription = "Reason for kicking the member"
kickCommandResponse = "{member} has been kicked from the server. Reason: {reason}"
kickCommandResponseNoReason = "{member} has been kicked from the server."
# ban
banCommandName = "ban"
banCommandDescription = "Bans user from the server"
banCommandMemberDescription = "Member to ban"
banCommandReasonDescription = "Reason for banning the member"
banCommandResponse = "{member} has been banned from the server. Reason: {reason}"
banCommandResponseNoReason = "{member} has been banned from the server."
banCommandTime = "delete_messages"
banCommandTimeDescription = "How many messages to delete based on time."
banCommandTimeNone = "Don't delete any messages"
banCommandTime1hr = "Previous hour"
banCommandTime6hr = "Previous 6 hours"
banCommandTime12hr = "Previous 12 hours"
banCommandTime24hr = "Previous 24 hours"
banCommandTime3d = "Previous 3 days"
banCommandTime7d = "Previous 7 days"
# unban
unbanCommandName = "unban"
unbanCommandDescription = "Unbans user from the server"
unbanCommandMemberDescription = "Member to unban"
unbanCommandResponse = "{member} has been unbanned from the server."
# timeout
timeoutCommandName = "timeout"
timeoutCommandDescription = "Timeouts (mutes) server member for a set time"
timeoutCommandMemberDescription = "Member to timeout"
timeoutCommandReasonDescription = "Reason for timeout"
timeoutCommandResponse = "{member} has been timed out for `{time}`. Reason: {reason}"
timeoutCommandResponseNoReason = "{member} has been timed out for {time}."
timeoutCommandTime = "timeout_duration"
timeoutCommandTimeDescription = "Duration of the timeout."
timeoutCommandTime10m = "10 minutes"
timeoutCommandTime30m = "30 minutes"
timeoutCommandTime1hr = "1 hour"
timeoutCommandTime3hr = "3 hours"
timeoutCommandTime6hr = "6 hours"
timeoutCommandTime12hr = "12 hours"
timeoutCommandTime24hr = "24 hours"
timeoutCommandTime3d = "3 days"
timeoutCommandTime7d = "7 days"