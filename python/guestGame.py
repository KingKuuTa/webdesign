guest = ['kofi', 'kaka', 'ronaldo']
print(f"{guest[0].upper()}   you have been invited to a birthday party")
print(f"{guest[1].upper()}   you have been invited to a birthday party")
print(f"{guest[2].upper()}   you have been invited to a birthday party")

print(f"\n{guest[0].title()} could not make it ")
del guest[0]
guest.insert(0, 'afforkor')


print(f"{guest[0].title()}  you have been invited to a birthday party")
print(f"{guest[1].title()}  you have been invited to a birthday party")
print(f"{guest[2].title()}  you have been invited to a birthday party")
