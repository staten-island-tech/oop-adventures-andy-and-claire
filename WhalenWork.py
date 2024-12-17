for mon in data['data']:
    try:
        if "Fighting" in mon['types']:
            print(mon['name'])
    except:
        continue

#Check in the assessment(pokemon)