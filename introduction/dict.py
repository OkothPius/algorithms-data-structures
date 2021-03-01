capitals = {'Uganda':'Kampala', 'Kenya':'Nairobi', 'Tanzania':'Dodoma'}
capitals['France']='Paris'

for k in capitals:
    print(capitals[k], " is the capital of ", k + ".")


phone_ext = {'david':1410, 'brad':1137}
print(phone_ext.keys())
print(phone_ext.values())
print(phone_ext.items())
print(phone_ext.get("kent"))
print(phone_ext.get("david", 1410))

