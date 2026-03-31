## -- Generic terms --
genericMember = "member"
genericReason = "reason"
## -- Error messages --
errorNoPermission = "You don't have permission to use this command."
errorForbidden = "I don't have permission to perform this action."
errorUnexpected = "An unexpected error occurred while executing the command."
## -- Utility commands --
# ping
pingCommandName = "ping"
pingCommandDescription = "Check the bot's latency"
pingCommandResponse = "Pong! Bot's latency is {latency} ms."
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