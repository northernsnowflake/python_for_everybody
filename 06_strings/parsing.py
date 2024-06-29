data = 'From stephen.marquard@utc.at.za Sat Jan 5 09:14:16 2008'

atpos = data.find('@') # tam, kde je zavináč
print(atpos)

sppos = data.find(' ',atpos) # najdi první mezeru v stpost. Atpost je tady jako první argument tj. odkud má hledání začít. 
print(sppos) # find vrací první výskyt hodnoty 

host = data[atpos + 1 : sppos] # do 1. mezery 
print(host)