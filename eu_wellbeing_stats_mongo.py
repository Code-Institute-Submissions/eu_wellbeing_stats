import pymongo

def mongo_connect():
    try:
        conn = pymongo.MongoClient()
        print "Mongo is connected!"
        return conn
    except pymongo.errors.ConnectionFailure, e:
        print "Could not connect to MongoDB: %s" % e

conn = mongo_connect()
db = conn['eu_wellbeing_stats']
coll = db.my_collection
coll.drop()

countries = [
    {
        "country": "Austria",
        "life_satisfaction": "7.1",
        "soc_support": "93",
        "life_expectancy": "72.0",
        "good_health": "69.5",
        "unemployment_rate": "5.7",
        "feel_safe": "81",
        "life_is_worthwhile": {"agree": "46", "strongly_agree": "38"},
        "mental_health_index": "66",
        "pers_relationships_satisfaction": "59.2",
        "job_satisfaction": "42.2",
        "green_areas_satisfaction": "56.1",
        "close_to_neighbours": {"agree": "38", "strongly_agree": "24"},
        "accommodation_satisfaction": "53.4",
        "risk_of_poverty": "13.9",
        "net_income": "21981",
        "finances_satisfaction": "26.0",
        "ends_meet": "13.4",
        "happiness": {"extremely_unhappy": "1.0", "1":"1.0", "2": "1.7", "3": "2.4", "4": "2.7", "5": "7.4",
                      "6": "7.6", "7": "22.3", "8": "26.5", "9": "15.1", "extremely_happy": "12.4"},
        "loneliness": "6.2"
    },
    {
        "country": "Belgium",
        "life_satisfaction": "6.9",
        "soc_support": "88",
        "life_expectancy": "71.1",
        "good_health": "75.0",
        "unemployment_rate": "8.5",
        "feel_safe": "72",
        "life_is_worthwhile": {"agree": "65", "strongly_agree": "16"},
        "mental_health_index": "65",
        "pers_relationships_satisfaction": "28.6",
        "job_satisfaction": "23.0",
        "green_areas_satisfaction": "23.0",
        "close_to_neighbours": {"agree": "48", "strongly_agree": "17"},
        "accommodation_satisfaction": "31.4",
        "risk_of_poverty": "14.9",
        "net_income": "19921",
        "finances_satisfaction": "16.0",
        "ends_meet": "20.5",
        "happiness": {"extremely_unhappy": "0.2", "1": "0.0", "2": "0.5", "3": "1.3", "4": "1.2", "5": "4.7",
                      "6": "5.6", "7": "20.5", "8": "38.5", "9": "18.9", "extremely_happy": "8.6"},
        "loneliness": "6.6"
    },
    {
        "country": "Czech Republic",
        "life_satisfaction": "6.6",
        "soc_support": "90",
        "life_expectancy": "69.4",
        "good_health": "60.7",
        "unemployment_rate": "5.1",
        "feel_safe": "61",
        "life_is_worthwhile": {"agree": "54", "strongly_agree": "20"},
        "mental_health_index": "62",
        "pers_relationships_satisfaction": "47.7",
        "job_satisfaction": "29.6",
        "green_areas_satisfaction": "35.5",
        "close_to_neighbours": {"agree": "46", "strongly_agree": "20"},
        "accommodation_satisfaction": "38.9",
        "risk_of_poverty": "9.7",
        "net_income": "11652",
        "finances_satisfaction": "12.3",
        "ends_meet": "26.6",
        "happiness": {"extremely_unhappy": "0.9", "1": "0.6", "2": "1.3", "3": "2.5", "4": "4.8", "5": "13.8",
                      "6": "12.8", "7": "18.7", "8": "24.1", "9": "12.9", "extremely_happy": "7.6"},
        "loneliness": "11.3"
    },
    {
        "country": "Bulgaria",
        "life_expectancy": "66.4",
        "life_is_worthwhile": {"agree": "49", "strongly_agree": "25"},
        "mental_health_index": "64",
        "pers_relationships_satisfaction": "14.6",
        "job_satisfaction": "16.1",
        "green_areas_satisfaction": "9.8",
        "close_to_neighbours": {"agree": "43", "strongly_agree": "31"},
        "accommodation_satisfaction": "18.2",
        "risk_of_poverty": "22.0",
        "net_income": "6882",
        "finances_satisfaction": "2.8",
        "ends_meet": "64.0"
    },
    {
        "country": "Croatia",
        "life_expectancy": "69.4",
        "life_is_worthwhile": {"agree": "48", "strongly_agree": "36"},
        "mental_health_index": "62",
        "pers_relationships_satisfaction": "29.5",
        "job_satisfaction": "25.6",
        "green_areas_satisfaction": "15.7",
        "close_to_neighbours": {"agree": "43", "strongly_agree": "35"},
        "accommodation_satisfaction": "23.9",
        "risk_of_poverty": "20.0",
        "net_income": "8259",
        "finances_satisfaction": "6.0",
        "ends_meet": "54.2"
    },
    {
        "country": "Cyprus",
        "life_expectancy": "71.3",
        "life_is_worthwhile": {"agree": "42", "strongly_agree": "33"},
        "mental_health_index": "61",
        "pers_relationships_satisfaction": "45.3",
        "job_satisfaction": "28.2",
        "green_areas_satisfaction": "10.5",
        "close_to_neighbours": {"agree": "32", "strongly_agree": "49"},
        "accommodation_satisfaction": "35.1",
        "risk_of_poverty": "16.2",
        "net_income": "15313",
        "finances_satisfaction": "5.9",
        "ends_meet": "58.8"
    },
    {
        "country": "Denmark",
        "life_satisfaction": "7.5",
        "soc_support": "96",
        "life_expectancy": "71.2",
        "good_health": "72.4",
        "unemployment_rate": "6.2",
        "feel_safe": "80",
        "life_is_worthwhile": {"agree": "30", "strongly_agree": "62"},
        "mental_health_index": "70",
        "pers_relationships_satisfaction": "56.8",
        "job_satisfaction": "44.4",
        "green_areas_satisfaction": "53.0",
        "close_to_neighbours": {"agree": "33", "strongly_agree": "34"},
        "accommodation_satisfaction": "53.8",
        "risk_of_poverty": "12.2",
        "net_income": "20384",
        "finances_satisfaction": "37.7",
        "ends_meet": "10.4",
        "happiness": {"extremely_unhappy": "0.1", "1": "0.4", "2": "0.8", "3": "1.2", "4": "1.0", "5": "3.1",
                      "6": "4.0", "7": "11.6", "8": "30.6", "9": "28.5", "extremely_happy": "18.7"},
        "loneliness": "3.4"
    },
    {
        "country": "Estonia",
        "life_satisfaction": "5.6",
        "soc_support": "90",
        "life_expectancy": "69.0",
        "good_health": "51.8",
        "unemployment_rate": "6.2",
        "feel_safe": "65",
        "life_is_worthwhile": {"agree": "57", "strongly_agree": "21"},
        "mental_health_index": "58",
        "pers_relationships_satisfaction": "36.9",
        "job_satisfaction": "26.6",
        "green_areas_satisfaction": "24.8",
        "close_to_neighbours": {"agree": "46", "strongly_agree": "32"},
        "accommodation_satisfaction": "25.0",
        "risk_of_poverty": "21.6",
        "net_income": "10432",
        "finances_satisfaction": "7.5",
        "ends_meet": "16.2",
        "happiness": {"extremely_unhappy": "0.6", "1": "0.4", "2": "1.5", "3": "3.3", "4": "3.8", "5": "13.7",
                      "6": "10.8", "7": "20.7", "8": "23.0", "9": "12.6", "extremely_happy": "9.7"},
        "loneliness": "7.3"
    },
    {
        "country": "Finland",
        "life_satisfaction": "7.4",
        "soc_support": "94",
        "life_expectancy": "71.0",
        "good_health": "69.2",
        "unemployment_rate": "9.4",
        "feel_safe": "81",
        "life_is_worthwhile": {"agree": "53", "strongly_agree": "37"},
        "mental_health_index": "66",
        "pers_relationships_satisfaction": "49.1",
        "job_satisfaction": "40.8",
        "green_areas_satisfaction": "47.5",
        "close_to_neighbours": {"agree": "17", "strongly_agree": "45"},
        "accommodation_satisfaction": "54.2",
        "risk_of_poverty": "12.4",
        "net_income": "19430",
        "finances_satisfaction": "28.6",
        "ends_meet": "7.0",
        "happiness": {"extremely_unhappy": "0.1", "1": "0.1", "2": "0.3", "3": "0.8", "4": "0.9", "5": "3.5",
                      "6": "4.1", "7": "14.8", "8": "35.4", "9": "31.3", "extremely_happy": "8.6"},
        "loneliness": "3.1"
    },
    {
        "country": "France",
        "life_satisfaction": "6.4",
        "soc_support": "89",
        "life_expectancy": "72.6",
        "good_health": "68.1",
        "unemployment_rate": "10.4",
        "feel_safe": "70",
        "life_is_worthwhile": {"agree": "52", "strongly_agree": "29"},
        "mental_health_index": "61",
        "pers_relationships_satisfaction": "34.0",
        "job_satisfaction": "20.0",
        "green_areas_satisfaction": "25.8",
        "close_to_neighbours": {"agree": "38", "strongly_agree": "30"},
        "accommodation_satisfaction": "26.3",
        "risk_of_poverty": "13.6",
        "net_income": "19885",
        "finances_satisfaction": "10.4",
        "ends_meet": "19.9",
        "happiness": {"extremely_unhappy": "0.5", "1": "0.2", "2": "0.9", "3": "1.6", "4": "2.6", "5": "9.7",
                      "6": "9.2", "7": "20.7", "8": "31.2", "9": "14.7", "extremely_happy": "8.9"},
        "loneliness": "9.6"
    },
    {
        "country": "Germany",
        "life_satisfaction": "7.0",
        "soc_support": "92",
        "life_expectancy": "71.3",
        "good_health": "65.2",
        "unemployment_rate": "4.6",
        "feel_safe": "80",
        "life_is_worthwhile": {"agree": "48", "strongly_agree": "28"},
        "mental_health_index": "66",
        "pers_relationships_satisfaction": "45.0",
        "job_satisfaction": "25.0",
        "green_areas_satisfaction": "40.3",
        "close_to_neighbours": {"agree": "35", "strongly_agree": "23"},
        "accommodation_satisfaction": "37.8",
        "risk_of_poverty": "16.7",
        "net_income": "20365",
        "finances_satisfaction": "18.7",
        "ends_meet": "7.6",
        "happiness": {"extremely_unhappy": "0.4", "1": "0.4", "2": "0.7", "3": "1.9", "4": "2.6", "5": "7.6",
                      "6": "6.3", "7": "17.4", "8": "31.8", "9": "19.5", "extremely_happy": "11.3"},
        "loneliness": "4.0"
    },
    {
        "country": "Greece",
        "life_satisfaction": "5.6",
        "soc_support": "83",
        "life_expectancy": "71.9",
        "good_health": "73.5",
        "unemployment_rate": "25.0",
        "feel_safe": "62",
        "life_is_worthwhile": {"agree": "37", "strongly_agree": "11"},
        "mental_health_index": "58",
        "pers_relationships_satisfaction": "25.2",
        "job_satisfaction": "14.0",
        "green_areas_satisfaction": "16.9",
        "close_to_neighbours": {"agree": "47", "strongly_agree": "22"},
        "accommodation_satisfaction": "19.0",
        "risk_of_poverty": "21.4",
        "net_income": "8802",
        "finances_satisfaction": "3.8",
        "ends_meet": "77.7"
    },
    {
        "country": "Hungary",
        "life_satisfaction": "5.3",
        "soc_support": "82",
        "life_expectancy": "67.4",
        "good_health": "57.5",
        "unemployment_rate": "6.8",
        "feel_safe": "47",
        "life_is_worthwhile": {"agree": "47", "strongly_agree": "21"},
        "mental_health_index": "61",
        "pers_relationships_satisfaction": "33.8",
        "job_satisfaction": "23.0",
        "green_areas_satisfaction": "15.1",
        "close_to_neighbours": {"agree": "46", "strongly_agree": "22"},
        "accommodation_satisfaction": "20.0",
        "risk_of_poverty": "14.9",
        "net_income": "7919",
        "finances_satisfaction": "6.1",
        "ends_meet": "46.6",
        "happiness": {"extremely_unhappy": "0.9", "1": "0.7", "2": "3.1", "3": "6.9", "4": "6.0", "5": "17.2",
                      "6": "13.3", "7": "18.6", "8": "16.8", "9": "8.0", "extremely_happy": "8.5"},
        "loneliness": "11.0"
    },
    {
        "country": "Iceland",
        "life_satisfaction": "7.5",
        "soc_support": "96",
        "life_expectancy": "72.7",
        "good_health": "76.1",
        "unemployment_rate": "4.0",
        "feel_safe": "78",
        "life_is_worthwhile": {"agree": "55", "strongly_agree": "38"},
        "mental_health_index": "69",
        "pers_relationships_satisfaction": "43.2",
        "job_satisfaction": "42.3",
        "green_areas_satisfaction": "43.8",
        "close_to_neighbours": {"agree": "53", "strongly_agree": "23"},
        "accommodation_satisfaction": "47.3",
        "risk_of_poverty": "9.6",
        "net_income": "20077",
        "finances_satisfaction": "18.4",
        "ends_meet": "19.8"
    },
    {
        "country": "Ireland",
        "life_satisfaction": "6.8",
        "soc_support": "95",
        "life_expectancy": "71.5",
        "good_health": "82.5",
        "unemployment_rate": "9.5",
        "feel_safe": "75",
        "life_is_worthwhile": {"agree": "64", "strongly_agree": "26"},
        "mental_health_index": "64",
        "pers_relationships_satisfaction": "60.3",
        "job_satisfaction": "28.3",
        "green_areas_satisfaction": "39.7",
        "close_to_neighbours": {"agree": "49", "strongly_agree": "24"},
        "accommodation_satisfaction": "48.0",
        "risk_of_poverty": "16.3",
        "net_income": "17704",
        "finances_satisfaction": "12.2",
        "ends_meet": "32.0",
        "happiness": {"extremely_unhappy": "0.4", "1": "0.4", "2": "1.2", "3": "2.1", "4": "3.2", "5": "8.6",
                      "6": "9.9", "7": "18.6", "8": "31.2", "9": "14.5", "extremely_happy": "9.9"},
        "loneliness": "4.6"
    },
    {
        "country": "Italy",
        "life_satisfaction": "5.8",
        "soc_support": "91",
        "life_expectancy": "72.8",
        "good_health": "67.9",
        "unemployment_rate": "11.9",
        "feel_safe": "58",
        "life_is_worthwhile": {"agree": "57", "strongly_agree": "22"},
        "mental_health_index": "64",
        "pers_relationships_satisfaction": "22.5",
        "job_satisfaction": "20.2",
        "green_areas_satisfaction": "12.9",
        "close_to_neighbours": {"agree": "49", "strongly_agree": "16"},
        "accommodation_satisfaction": "22.9",
        "risk_of_poverty": "19.9",
        "net_income": "15395",
        "finances_satisfaction": "5.9",
        "ends_meet": "37.9"
    },
    {
        "country": "Latvia",
        "life_satisfaction": "5.9",
        "soc_support": "84",
        "life_expectancy": "67.1",
        "good_health": "45.8",
        "unemployment_rate": "9.9",
        "life_is_worthwhile": {"agree": "50", "strongly_agree": "24"},
        "mental_health_index": "56",
        "pers_relationships_satisfaction": "41.3",
        "job_satisfaction": "25.8",
        "green_areas_satisfaction": "32.7",
        "close_to_neighbours": {"agree": "42", "strongly_agree": "36"},
        "accommodation_satisfaction": "16.8",
        "risk_of_poverty": "22.5",
        "net_income": "8092",
        "finances_satisfaction": "4.0",
        "ends_meet": "42.7"
    },
    {
        "country": "Lithuania",
        "life_expectancy": "66.1",
        "good_health": "44.9",
        "life_is_worthwhile": {"agree": "53", "strongly_agree": "16"},
        "mental_health_index": "58",
        "pers_relationships_satisfaction": "44.9",
        "job_satisfaction": "29.6",
        "green_areas_satisfaction": "32.8",
        "close_to_neighbours": {"agree": "51", "strongly_agree": "15"},
        "accommodation_satisfaction": "30.6",
        "risk_of_poverty": "22.2",
        "net_income": "8251",
        "finances_satisfaction": "8.8",
        "ends_meet": "28.9",
        "happiness": {"extremely_unhappy": "0.7", "1": "0.8", "2": "2.5", "3": "5.6", "4": "7.3", "5": "16.2",
                      "6": "11.0", "7": "18.0", "8": "23.3", "9": "10.4", "extremely_happy": "4.3"},
        "loneliness": "7.8"
    },
    {
        "country": "Luxembourg",
        "life_satisfaction": "6.7",
        "soc_support": "93",
        "life_expectancy": "71.8",
        "good_health": "72.8",
        "unemployment_rate": "6.5",
        "feel_safe": "68",
        "life_is_worthwhile": {"agree": "51", "strongly_agree": "37"},
        "mental_health_index": "63",
        "pers_relationships_satisfaction": "40.1",
        "job_satisfaction": "30.4",
        "green_areas_satisfaction": "38.7",
        "close_to_neighbours": {"agree": "36", "strongly_agree": "37"},
        "accommodation_satisfaction": "38.4",
        "risk_of_poverty": "15.3",
        "net_income": "29285",
        "finances_satisfaction": "21.5",
        "ends_meet": "12.4"
    },
    {
        "country": "Netherlands",
        "life_satisfaction": "7.3",
        "soc_support": "88",
        "life_expectancy": "72.2",
        "good_health": "77.3",
        "unemployment_rate": "6.9",
        "feel_safe": "81",
        "life_is_worthwhile": {"agree": "64", "strongly_agree": "28"},
        "mental_health_index": "65",
        "pers_relationships_satisfaction": "40.5",
        "job_satisfaction": "22.9",
        "green_areas_satisfaction": "34.4",
        "close_to_neighbours": {"agree": "57", "strongly_agree": "21"},
        "accommodation_satisfaction": "34.7",
        "risk_of_poverty": "11.6",
        "net_income": "19387",
        "finances_satisfaction": "21.9",
        "ends_meet": "12.7",
        "happiness": {"extremely_unhappy": "0.1", "1":"0.0", "2": "0.3", "3": "0.8", "4": "1.0", "5": "2.3",
                      "6": "5.2", "7": "21.1", "8": "41.1", "9": "20.2", "extremely_happy": "7.8"},
        "loneliness": "2.7"
    },
    {
        "country": "Malta",
        "life_expectancy": "71.7",
        "life_is_worthwhile": {"agree": "64", "strongly_agree": "24"},
        "mental_health_index": "58",
        "pers_relationships_satisfaction": "55.3",
        "job_satisfaction": "28.0",
        "green_areas_satisfaction": "27.2",
        "close_to_neighbours": {"agree": "43", "strongly_agree": "23"},
        "accommodation_satisfaction": "39.3",
        "risk_of_poverty": "16.3",
        "net_income": "16681",
        "finances_satisfaction": "9.0",
        "ends_meet": "21.5"
    },
    {
        "country": "Norway",
        "life_satisfaction": "7.6",
        "soc_support": "93",
        "life_expectancy": "72.0",
        "good_health": "78.5",
        "unemployment_rate": "4.4",
        "feel_safe": "86",
        "pers_relationships_satisfaction": "51.5",
        "job_satisfaction": "39.1",
        "green_areas_satisfaction": "54.8",
        "accommodation_satisfaction": "40.1",
        "risk_of_poverty": "11.9",
        "net_income": "28323",
        "finances_satisfaction": "33.1",
        "ends_meet": "5.1",
        "happiness": {"extremely_unhappy": "0.1", "1": "0.2", "2": "0.7", "3": "1.2", "4": "1.4", "5": "4.7",
                      "6": "5.5", "7": "15.5", "8": "30.9", "9": "24.8", "extremely_happy": "15.1"},
        "loneliness": "3.7"
    },
    {
        "country": "Poland",
        "life_satisfaction": "6.0",
        "soc_support": "86",
        "life_expectancy": "68.7",
        "good_health": "58.1",
        "unemployment_rate": "7.5",
        "feel_safe": "63",
        "life_is_worthwhile": {"agree": "55", "strongly_agree": "17"},
        "mental_health_index": "59",
        "pers_relationships_satisfaction": "44.4",
        "job_satisfaction": "32.0",
        "green_areas_satisfaction": "39.1",
        "close_to_neighbours": {"agree": "50", "strongly_agree": "16"},
        "accommodation_satisfaction": "36.3",
        "risk_of_poverty": "17.6",
        "net_income": "9950",
        "finances_satisfaction": "13.0",
        "ends_meet": "29.4",
        "happiness": {"extremely_unhappy": "0.5", "1": "0.7", "2": "1.3", "3": "2.7", "4": "3.0", "5": "13.6",
                      "6": "7.4", "7": "17.0", "8": "25.8", "9": "15.2", "extremely_happy": "13.0"},
        "loneliness": "11.7"
    },
    {
        "country": "Portugal",
        "life_satisfaction": "5.1",
        "soc_support": "85",
        "life_expectancy": "71.4",
        "good_health": "45.9",
        "unemployment_rate": "12.7",
        "feel_safe": "72",
        "life_is_worthwhile": {"agree": "54", "strongly_agree": "20"},
        "mental_health_index": "66",
        "pers_relationships_satisfaction": "41.5",
        "job_satisfaction": "24.5",
        "green_areas_satisfaction": "17.7",
        "close_to_neighbours": {"agree": "48", "strongly_agree": "23"},
        "accommodation_satisfaction": "31.9",
        "risk_of_poverty": "19.5",
        "net_income": "10317",
        "finances_satisfaction": "3.9",
        "ends_meet": "40.4",
        "happiness": {"extremely_unhappy": "1.5", "1": "0.9", "2": "1.1", "3": "3.7", "4": "3.7", "5": "14.7",
                      "6": "10.7", "7": "17.0", "8": "23.2", "9": "9.4", "extremely_happy": "14.1"},
        "loneliness": "9.8"
    },
    {
        "country": "Serbia",
        "life_expectancy": "67.7",
        "life_is_worthwhile": {"agree": "47", "strongly_agree": "34"},
        "mental_health_index": "54",
        "pers_relationships_satisfaction": "54.5",
        "job_satisfaction": "18.8",
        "green_areas_satisfaction": "15.8",
        "close_to_neighbours": {"agree": "44", "strongly_agree": "32"},
        "accommodation_satisfaction": "18.0",
        "risk_of_poverty": "25.4",
        "net_income": "5042",
        "finances_satisfaction": "3.6",
        "ends_meet": "64.7"
    },
    {
        "country": "Slovakia",
        "life_satisfaction": "6.2",
        "soc_support": "92",
        "life_expectancy": "68.1",
        "good_health": "64.7",
        "unemployment_rate": "11.5",
        "feel_safe": "56",
        "life_is_worthwhile": {"agree": "49", "strongly_agree": "20"},
        "mental_health_index": "59",
        "pers_relationships_satisfaction": "43.6",
        "job_satisfaction": "29.2",
        "green_areas_satisfaction": "22.2",
        "close_to_neighbours": {"agree": "47", "strongly_agree": "19"},
        "accommodation_satisfaction": "38.4",
        "risk_of_poverty": "12.3",
        "net_income": "10220",
        "finances_satisfaction": "10.3",
        "ends_meet": "32.7"
    },
    {
        "country": "Romania",
        "life_expectancy": "66.8",
        "life_is_worthwhile": {"agree": "44", "strongly_agree": "36"},
        "mental_health_index": "57",
        "pers_relationships_satisfaction": "30.6",
        "job_satisfaction": "20.4",
        "green_areas_satisfaction": "23.8",
        "close_to_neighbours": {"agree": "42", "strongly_agree": "38"},
        "accommodation_satisfaction": "28.3",
        "risk_of_poverty": "25.4",
        "net_income": "4357",
        "finances_satisfaction": "8.2",
        "ends_meet": "45.6"
    },
    {
        "country": "Slovenia",
        "life_satisfaction": "5.7",
        "soc_support": "89",
        "life_expectancy": "71.1",
        "good_health": "64.8",
        "unemployment_rate": "9.0",
        "feel_safe": "84",
        "life_is_worthwhile": {"agree": "48", "strongly_agree": "26"},
        "mental_health_index": "58",
        "pers_relationships_satisfaction": "51.8",
        "job_satisfaction": "29.1",
        "green_areas_satisfaction": "44.7",
        "close_to_neighbours": {"agree": "49", "strongly_agree": "26"},
        "accommodation_satisfaction": "36.2",
        "risk_of_poverty": "14.3",
        "net_income": "15102",
        "finances_satisfaction": "7.9",
        "ends_meet": "28.7",
        "happiness": {"extremely_unhappy": "0.6", "1": "0.6", "2": "1.4", "3": "2.8", "4": "4.1", "5": "15.0",
                      "6": "7.9", "7": "16.4", "8": "25.5", "9": "14.2", "extremely_happy": "11.4"},
        "loneliness": "6.0"
    },
    {
        "country": "Sweden",
        "life_satisfaction": "7.3",
        "soc_support": "92",
        "life_expectancy": "72.0",
        "good_health": "80.1",
        "unemployment_rate": "7.4",
        "feel_safe": "76",
        "life_is_worthwhile": {"agree": "43", "strongly_agree": "47"},
        "mental_health_index": "64",
        "pers_relationships_satisfaction": "46.8",
        "job_satisfaction": "33.8",
        "green_areas_satisfaction": "54.1",
        "close_to_neighbours": {"agree": "32", "strongly_agree": "40"},
        "accommodation_satisfaction": "49.3",
        "risk_of_poverty": "14.5",
        "net_income": "21216",
        "finances_satisfaction": "35.5",
        "ends_meet": "5.4",
        "happiness": {"extremely_unhappy": "0.1", "1": "0.1", "2": "0.3", "3": "0.8", "4": "1.5", "5": "4.4",
                      "6": "6.4", "7": "18.1", "8": "32.8", "9": "23.6", "extremely_happy": "11.9"},
        "loneliness": "4.9"
    },
    {
        "country": "Spain",
        "life_satisfaction": "6.4",
        "soc_support": "96",
        "life_expectancy": "72.4",
        "good_health": "72.6",
        "unemployment_rate": "22.1",
        "feel_safe": "85",
        "life_is_worthwhile": {"agree": "52", "strongly_agree": "30"},
        "mental_health_index": "65",
        "pers_relationships_satisfaction": "36.0",
        "job_satisfaction": "19.4",
        "green_areas_satisfaction": "18.8",
        "close_to_neighbours": {"agree": "41", "strongly_agree": "38"},
        "accommodation_satisfaction": "23.8",
        "risk_of_poverty": "22.1",
        "net_income": "14463",
        "finances_satisfaction": "7.4",
        "ends_meet": "35.2",
        "happiness": {"extremely_unhappy": "0.4", "1": "0.4", "2": "0.9", "3": "1.9", "4": "2.1", "5": "8.8",
                      "6": "9.5", "7": "20.7", "8": "28.2", "9": "14.3", "extremely_happy": "12.7"},
        "loneliness": "8.5"
    },
    {
        "country": "Switzerland",
        "life_satisfaction": "7.6",
        "soc_support": "93",
        "life_expectancy": "73.1",
        "good_health": "79.3",
        "unemployment_rate": "4.5",
        "feel_safe": "81",
        "pers_relationships_satisfaction": "57.6",
        "job_satisfaction": "36.6",
        "green_areas_satisfaction": "54.0",
        "accommodation_satisfaction": "51.9",
        "risk_of_poverty": "15.6",
        "net_income": "26590",
        "finances_satisfaction": "32.8",
        "ends_meet": "11.2",
        "happiness": {"extremely_unhappy": "0.1", "1": "0.1", "2": "0.3", "3": "0.9", "4": "1.3", "5": "3.9",
                      "6": "5.4", "7": "13.5", "8": "32.4", "9": "26.1", "extremely_happy": "16.0"},
        "loneliness": "3.7"
    },
    {
        "country": "Turkey",
        "life_satisfaction": "5.5",
        "soc_support": "84",
        "life_expectancy": "66.2",
        "good_health": "68.1",
        "unemployment_rate": "10.3",
        "feel_safe": "60",
        "life_is_worthwhile": {"agree": "52", "strongly_agree": "23"},
        "mental_health_index": "56",
        "pers_relationships_satisfaction": "33.3",
        "job_satisfaction": "18.3",
        "green_areas_satisfaction": "17.7",
        "close_to_neighbours": {"agree": "40", "strongly_agree": "32"},
        "accommodation_satisfaction": "13.2",
        "risk_of_poverty": "23.0",
        "net_income": "5,456",
        "finances_satisfaction": "6.4",
        "ends_meet": "19.3"
    },
    {
        "country": "United Kingdom",
        "life_satisfaction": "6.5",
        "soc_support": "93",
        "life_expectancy": "71.4",
        "good_health": "70.0",
        "unemployment_rate": "5.3",
        "feel_safe": "79",
        "life_is_worthwhile": {"agree": "60", "strongly_agree": "22"},
        "mental_health_index": "59",
        "pers_relationships_satisfaction": "57.5",
        "job_satisfaction": "28.0",
        "green_areas_satisfaction": "36.5",
        "close_to_neighbours": {"agree": "44", "strongly_agree": "15"},
        "accommodation_satisfaction": "44.4",
        "risk_of_poverty": "16.7",
        "net_income": "17712",
        "finances_satisfaction": "18.5",
        "ends_meet": "16.4",
        "happiness": {"extremely_unhappy": "0.7", "1": "0.4", "2": "1.1", "3": "2.6", "4": "2.2", "5": "6.3",
                      "6": "7.6", "7": "18.0", "8": "28.3", "9": "19.2", "extremely_happy": "13.7"},
        "loneliness": "5.0"
    }
]

coll.insert(countries)



