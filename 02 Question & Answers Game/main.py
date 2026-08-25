try:
    questions = [
    ["Which agreement, signed in 1954 between India and China, laid out the 'Five Principles of Peaceful Coexistence'?", "Panchsheel Agreement", "Shimla Agreement", "Tashkent Declaration", "Lahore Declaration", 1],
    ["India conducted its first nuclear test, codenamed 'Smiling Buddha,' in which year?", "1971", "1974", "1980", "1998", 2],
    ["The Tashkent Declaration of 1966 was signed between India and Pakistan after which war?", "1962 Indo-China War", "1965 Indo-Pak War", "1971 Indo-Pak War", "Kargil War", 2],
    ["Which Indian Prime Minister signed the Simla Agreement with Pakistan in 1972?", "Lal Bahadur Shastri", "Morarji Desai", "Indira Gandhi", "Jawaharlal Nehru", 3],
    ["India liberated Goa from Portuguese rule through which military operation in 1961?", "Operation Polo", "Operation Vijay", "Operation Trident", "Operation Cactus", 2],
    ["SAARC (South Asian Association for Regional Cooperation) was founded in which year?", "1980", "1985", "1991", "1995", 2],
    ["Which Indian state, formerly a monarchy, merged with India in 1975 after a referendum?", "Tripura", "Manipur", "Sikkim", "Mizoram", 3],
    ["India's 'Look East Policy,' aimed at strengthening ties with Southeast Asia, was launched in the early 1990s under which PM?", "Rajiv Gandhi", "V.P. Singh", "P.V. Narasimha Rao", "Atal Bihari Vajpayee", 3],
    ["The Quit India Movement, a major push for full independence, was launched by Gandhi in which year?", "1930", "1942", "1945", "1947", 2],
    ["Which mission, sent by the British in 1946, proposed a framework for India's transfer of power?", "Simon Commission", "Cripps Mission", "Cabinet Mission", "Mountbatten Plan", 3],
    ["Princely states acceded to the Indian Union after independence by signing which legal document?", "Treaty of Accession", "Instrument of Accession", "Government of India Act", "Act of Union", 2],
    ["India recognized Bangladesh's independence during the 1971 war, which was fought against which country?", "China", "Sri Lanka", "Pakistan", "Nepal", 3],
    ["Which treaty, signed in August 1971, gave India crucial strategic backing from the USSR ahead of the Bangladesh Liberation War?", "Indo-Soviet Treaty of Peace, Friendship and Cooperation", "Treaty of Tashkent", "Treaty of Lahore", "Treaty of Yalta", 1],
    ["India formally adopted a 'No First Use' nuclear doctrine after which event?", "Pokhran-I (1974)", "Pokhran-II (1998)", "The Kargil War (1999)", "Joining the NPT", 2],
    ["Who was the host of the first Non-Aligned Movement summit in Belgrade, 1961, and is considered one of its key founders alongside Nehru?", "Sukarno", "Josip Broz Tito", "Gamal Abdel Nasser", "Kwame Nkrumah", 2],
    ["India became a non-permanent member of the UN Security Council for the first time in which year?", "1947", "1950", "1965", "1972", 2],
    ]
    prizes = [100,200,300,400,500,600,700,800,900,1000,1100,1300,1500,1700,1900,2500]
    i = 0
    for question in questions:
        print(question[0])
        print(f"a. {question[1]}")
        print(f"b. {question[2]}")
        print(f"c. {question[3]}")
        print(f"d. {question[4]}")
    #  Check whether the answer is corect or not
        a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d\n"))
        if question[5] == a:
            print("Correct answer")
        else:
            print(f"Incorrect, The correct answer is {question[5]}")
            print("Better luck next time")
            break
        print(f"You won {prizes[i]}")
        i += 1

except:
    print("Please enter a valid option")
