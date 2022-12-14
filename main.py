import sys

file_save = True

file_name = sys.argv[1]

if sys.argv[2] == "-interactive":
    while True:
        print("-e, --exit")
        user_command = input(">> ")
        if user_command == "-e" or user_command == "--exit":
            exit()

        user_command = user_command.split()

        with open(file_name, 'r') as file:
            lines = file.readlines()

        lines = lines[1:]

        country = user_command[0]#take country

        year_city = {}
        for line in lines:
            line = line.split('\t')
            if line[6] == country or line[7]:
                year_city[int(line[9])] = line[11]


        min_year = min(year_city.keys())
        event_city = year_city[min_year]

        print(f"Перша участь -> {min_year}: {event_city}")


        olympics_medals = {}

        for line in lines:
            line = line.split('\t')
            if line[6] == country or line[7] == country:
                if line[14] != "NA\n" and line[14] != "NA":
                    if line[9] + " " + line[10] not in olympics_medals:
                        olympics_medals[line[9] + " " + line[10]] = 1
                    else:
                        olympics_medals[line[9] + " " + line[10]] += 1


        the_worst_olympic_medals = min(olympics_medals.values())#worst medals count #1
        the_best_olympic_medals = max(olympics_medals.values())#best medals count

        the_worst_olympic = ""#worst olympic name
        the_best_olympic = ""

        #run for dict
        for olymp in olympics_medals: #кожен ключ в olymp
            #olymp
                #olympics_medals[ '1998 Winter'] -> 1 == 1
            if olympics_medals[olymp] == the_worst_olympic_medals:# if
                the_worst_olympic = olymp
            if olympics_medals[olymp] == the_best_olympic_medals:
                the_best_olympic = olymp


        print("The worst olympic:", the_worst_olympic, "->", the_worst_olympic_medals, "medals count")
        print("The best olympic:", the_best_olympic, "->", the_best_olympic_medals, "medals count")


        olympics = {}

        for line in lines:
            line = line.split('\t')

            if line[6] == country or line[7] == country:
                if line[14] != "NA\n" and line[14] != "NA":
                    season = line[9] + " " + line[10]
                    if season not in olympics:
                        olympics[season] = {"Gold": 0, "Silver": 0, "Bronze": 0}
                        olympics[season][line[14][:-1]] += 1
                    else:
                        olympics[season][line[14][:-1]] += 1
        print()

        for olymp in olympics:
            print(f"{olymp}| Gold: {olympics[olymp]['Gold']}, Silver: {olympics[olymp]['Silver']}, Bronze: {olympics[olymp]['Bronze']}")




if sys.argv[2] == "-overall":


    with open(file_name, 'r') as file:
        lines = file.readlines()

    lines = lines[1:]

    if "-output" in sys.argv:
        result_file = open(sys.argv[sys.argv.index("-output") + 1], 'w')
        countries = sys.argv[3:sys.argv.index("-output")]
        file_save = False
    else:
        countries = sys.argv[3:]

    for country in countries:


        country_history = {}

        for line in lines:

            line = line.split("\t")
            if line[14] != "NA\n" and line[14] != "NA":
                if line[6] == country or line[7] == country:
                    years = country_history.keys()
                    if line[9] not in years:
                        country_history[line[9]] = 1
                    else:
                        country_history[line[9]] += 1

        current_year = list(country_history.keys())[0]
        medals = list(country_history.values())[0]

        for year in country_history:
            if country_history[year] > medals:
                medals = country_history[year]
                current_year = year

        if "-output" in sys.argv:
            print(country, current_year, medals)
            print(country, current_year, medals, file=result_file)

        else:
            print(country, current_year, medals)

    if "-output" in sys.argv:
        result_file.close()



file = open(file_name, 'r')
argument = sys.argv[2]
countries = sys.argv[3]
if argument == "-medals":
    years = sys.argv[4]
else:
    years = sys.argv[3]

if file_save:
    if "-output" in sys.argv:
        output_name = sys.argv[sys.argv.index("-output") + 1]
        output_file = open(output_name, 'w')


    line = file.readline()
    counter = 0
    c_gold = 0
    c_silver = 0
    c_bronze = 0
    dictionary = {}
    years_dictionary = {}
    while line:
        line = line[:-1]
        word = line.split('\t')
        country = word[6]
        country_code = word[7]
        year = word[9]
        if (country == countries or country_code == countries) and year == years:
            if counter < 10 and word[14] != "NA":
                counter += 1
                if word[14] == "Gold":
                    c_gold += 1
                elif word[14] == "Silver":
                    c_silver += 1
                elif word[14] == "Bronze":
                    c_bronze += 1
                if "-output" in sys.argv:
                    print(f"{word[1]}, {word[12]}, {word[14]}")
                    print(f"{word[1]}, {word[12]}, {word[14]}", file=output_file)
                else:
                    print(f"{word[1]}, {word[12]}, {word[14]}")

        if argument == "-total" and word[14] != "NA" and year == sys.argv[3]:
            keys = country
            values = ["Gold", "Silver", "Bronze"]
            # if country in dict, get list and add
            # else - add new list
            if country not in dictionary:
                dictionary[country] = [0, 0, 0]
                if values[0] == word[14]:
                    dictionary[country][0] = 1
                elif values[1] == word[14]:
                    dictionary[country][1] = 1
                elif values[2] == word[14]:
                    dictionary[country][2] = 1
            else:
                if country in dictionary:
                    if values[0] == word[14]:
                        dictionary[country][0] += 1
                    elif values[1] == word[14]:
                        dictionary[country][1] += 1
                    elif values[2] == word[14]:
                        dictionary[country][2] += 1
                    else:
                        dictionary[country] = 1

        curent_year = word[9]
        line = file.readline()

    if argument == "-medals":
        print(f"Gold:{c_gold}, Silver:{c_silver}, Bronze:{c_bronze}")


    if argument == "-total":
        for country in dictionary:
            if "-output" in sys.argv:
                print(
                    f"{country}\t\t Gold:{dictionary[country][0]}, Silver:{dictionary[country][1]}, Bronze:{dictionary[country][2]}")

                print(f"{country}\t\t Gold:{dictionary[country][0]}, Silver:{dictionary[country][1]}, Bronze:{dictionary[country][2]}", file=output_file)
            else:
                print(f"{country}\t\t Gold:{dictionary[country][0]}, Silver:{dictionary[country][1]}, Bronze:{dictionary[country][2]}")

    if "-output" in sys.argv:
        print(f"Gold:{c_gold}, Silver:{c_silver}, Bronze:{c_bronze}", file=output_file)
        output_file.close()