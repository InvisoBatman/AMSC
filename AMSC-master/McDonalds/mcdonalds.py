'''
    A program that expedites the McDonald's survey proccess
    Takes a survey receipt code and returns a completion code
'''
# imports
import re
import requests
import time


# main function
def main():
    print("Welcome to the Auto-McDonald's-Survey-Completer", end='\n\n')
    print("How to use:")
    print("1. Enter each receipt survey code you have (multiple receipts surveys may be entered in a single go)")
    print("2. After each receipt survey code, hit the ENTER key on your keyboard")
    print("3. After entering the last survey code hit CLTR + D")
    print("4. Record the survey completion codes on each receipt corresponding to their survey code")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ end of instructions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", end='\n\n')

    # a list for survey Validation Codes
    completion_codes = []

    # retrieve survey codes (a list)
    codes = get_codes()

    i = 1

    # complete survey at mcdvoice.com
    for code in codes:

        # complete a single survey, retrieve the completion code, and append it to the completion_codes list
        completion_codes.append(complete_survey(code))

        print(i)
        i += 1

    # print survey completion codes
    print_completion_code(codes, completion_codes)


'''A function that retrieves McDonald's receipt codes'''
def get_codes():
    # a list to store the user given codes
    codes = []

    # get an endless amount of survey codes until the user presses CTLR + D
    while True:
        try:
            code = str(input("Code: ")).strip()
        except EOFError:
            print("")
            print("thinking...")
            break
        else:
            if matches := re.search(r"^([0-9][0-9][0-9][0-9][0-9]-){5}([0-9]$)", code):
                codes.append(code)
            else:
                print("Invalid Code")

    return codes


'''A function that completes mcdvoice surveys'''
def complete_survey(code: str):

    survey_code = str()

    url = "https://mcdvoice.com/"

    with requests.Session() as s:
        response = s.get(url)

        url = find_survey_key(response.text)

        CN1, CN2, CN3, CN4, CN5, CN6 = code.split("-")

        # entering the survey receipt code
        body = {
            "JavaScriptEnabled": "1",
            "FIP": "True",
            "CN1": CN1,
            "CN2": CN2,
            "CN3": CN3,
            "CN4": CN4,
            "CN5": CN5,
            "CN6": CN6,
            "NextButton": "Start",
            "AllowCapture": "True"
        }

        # this could probably be apart of initialize_connection along with the variables it uses ^^^
        # submitting the survey code to the server and beginning the survey
        response = s.post(url, data = body)

        url = find_survey_key(response.text)

        body = {
            "R000455": "1",
            "IoNF": "4",
            "PostedFNS": "S000100|R000455",
            "OneQuestionLeftUnansweredErrorMessageTemplate": "There+is+{0}+error+on+the+page.",
            "MoreQuestionsLeftUnansweredErrorMessageTemplate": "There+are+{0}+errors+on+the+page."
        }

        response = s.post(url, data = body)

        # attention!!! FUTURE IAN!!! you should detect the progress of the survey by using regex to detect each survey question
        # good idea past Ian, I'm thinking I will create the skeleton first and maybe use this idea to clean things up if I add customization later

        url = find_survey_key(response.text)

        body = {
            "R004000": "1",
            "IoNF": "5",
            "PostedFNS": "R004000",
            "OneQuestionLeftUnansweredErrorMessageTemplate": "There+is+{0}+error+on+the+page.",
            "MoreQuestionsLeftUnansweredErrorMessageTemplate": "There+are+{0}+errors+on+the+page."
        }

        response = s.post(url, data = body)

        url = find_survey_key(response.text)

        body = {
            "R001000": "4",
            "IoNF": "7",
            "PostedFNS": "S000200|R001000",
            "OneQuestionLeftUnansweredErrorMessageTemplate": "There+is+{0}+error+on+the+page.",
            "MoreQuestionsLeftUnansweredErrorMessageTemplate": "There+are+{0}+errors+on+the+page."
        }

        response = s.post(url, data = body)

        url = find_survey_key(response.text)

        body = {
            "R000444": "2",
            "IoNF": "10",
            "PostedFNS": "R000444",
            "OneQuestionLeftUnansweredErrorMessageTemplate": "There+is+{0}+error+on+the+page.",
            "MoreQuestionsLeftUnansweredErrorMessageTemplate": "There+are+{0}+errors+on+the+page."
        }

        response = s.post(url, data = body)

        url = find_survey_key(response.text)

        body = {
            "R000473": "2",
            "IoNF": "11",
            "PostedFNS": "R000473",
            "OneQuestionLeftUnansweredErrorMessageTemplate": "There+is+{0}+error+on+the+page.",
            "MoreQuestionsLeftUnansweredErrorMessageTemplate": "There+are+{0}+errors+on+the+page."
        }

        response = s.post(url, data = body)

        url = find_survey_key(response.text)

        body = {
            "R007000": "4",
            "R005000": "4",
            "R009000": "4",
            "R000351": "4",
            "R008000": "4",
            "R006000": "4",
            "IoNF": "19",
            "PostedFNS": "R007000|R005000|R009000|R000351|R008000|R006000",
            "OneQuestionLeftUnansweredErrorMessageTemplate": "There+is+{0}+error+on+the+page.",
            "MoreQuestionsLeftUnansweredErrorMessageTemplate": "There+are+{0}+errors+on+the+page."
        }

        response = s.post(url, data = body)

        url = find_survey_key(response.text)

        body = {
            "R028000": "4",
            "R011000": "4",
            "R015000": "4",
            "IoNF": "23",
            "PostedFNS": "R028000|R011000|R015000",
            "OneQuestionLeftUnansweredErrorMessageTemplate": "There+is+{0}+error+on+the+page.",
            "MoreQuestionsLeftUnansweredErrorMessageTemplate": "There+are+{0}+errors+on+the+page."
        }

        response = s.post(url, data = body)

        url = find_survey_key(response.text)

        body = {
            "R000373Other": "",
            "IoNF": "71",
            "PostedFNS": "R000420|R000367|R000411|R000458|R000459|R000469|R000471|R000365|R000421|R000412|R000422|R000366|R000361|R000414|R000460|R000373",
            "OneQuestionLeftUnansweredErrorMessageTemplate": "There+is+{0}+error+on+the+page.",
            "MoreQuestionsLeftUnansweredErrorMessageTemplate": "There+are+{0}+errors+on+the+page."
        }

        response = s.post(url, data = body)

        url = find_survey_key(response.text)

        body = {
            "R016000": "2",
            "IoNF": "101",
            "PostedFNS": "R016000",
            "OneQuestionLeftUnansweredErrorMessageTemplate": "There+is+{0}+error+on+the+page.",
            "MoreQuestionsLeftUnansweredErrorMessageTemplate": "There+are+{0}+errors+on+the+page."
        }

        response = s.post(url, data = body)

        url = find_survey_key(response.text)

        body = {
            "R018000": "4",
            "R019000": "4",
            "IoNF": "119",
            "PostedFNS": "R018000|R019000",
            "OneQuestionLeftUnansweredErrorMessageTemplate": "There+is+{0}+error+on+the+page.",
            "MoreQuestionsLeftUnansweredErrorMessageTemplate": "There+are+{0}+errors+on+the+page."
        }

        response = s.post(url, data = body)

        url = find_survey_key(response.text)

        body = {
            "S080000": "",
            "IoNF": "127",
            "PostedFNS": "S080000",
            "OneQuestionLeftUnansweredErrorMessageTemplate": "There+is+{0}+error+on+the+page.",
            "MoreQuestionsLeftUnansweredErrorMessageTemplate": "There+are+{0}+errors+on+the+page."
        }

        response = s.post(url, data = body)

        url = find_survey_key(response.text)

        body = {
            "R000345": "2",
            "IoNF": "132",
            "PostedFNS": "R000345",
            "OneQuestionLeftUnansweredErrorMessageTemplate": "There+is+{0}+error+on+the+page.",
            "MoreQuestionsLeftUnansweredErrorMessageTemplate": "There+are+{0}+errors+on+the+page."
        }

        response = s.post(url, data = body)

        url = find_survey_key(response.text)

        body = {
            "R020000": "1",
            "IoNF": "145",
            "PostedFNS": "R020000",
            "OneQuestionLeftUnansweredErrorMessageTemplate": "There+is+{0}+error+on+the+page.",
            "MoreQuestionsLeftUnansweredErrorMessageTemplate": "There+are+{0}+errors+on+the+page."
        }

        response = s.post(url, data = body)

        url = find_survey_key(response.text)

        body = {
            "R000387": "4",
            "R000387Other": "",
            "IoNF": "146",
            "PostedFNS": "R000387",
            "OneQuestionLeftUnansweredErrorMessageTemplate": "There+is+{0}+error+on+the+page.",
            "MoreQuestionsLeftUnansweredErrorMessageTemplate": "There+are+{0}+errors+on+the+page."
        }

        response = s.post(url, data = body)

        url = find_survey_key(response.text)

        body = {
            "R000482": "4",
            "IoNF": "147",
            "PostedFNS": "R000482",
            "OneQuestionLeftUnansweredErrorMessageTemplate": "There+is+{0}+error+on+the+page.",
            "MoreQuestionsLeftUnansweredErrorMessageTemplate": "There+are+{0}+errors+on+the+page."
        }

        response = s.post(url, data = body)

        # this needs to be tested more
        survey_code = re.search(r'<p class="ValCode">Validation Code: ([0-9][0-9][0-9][0-9][0-9][0-9][0-9])</p>', response.text)

    time.sleep(10)

    return survey_code.group(1)


'''A function that prints the completed survey codes'''
def print_completion_code(codes: list, completion_codes: list):
    
    for i in range(len(codes)):
        print("Survey Code:", codes[i], "Validation Code:", completion_codes[i])
    
'''A function that finds the proper http url for the current survey and returns usable url'''
def find_survey_key(s: str):
    # a fresh mcvoice link for concatinating later
    mcd = "https://mcdvoice.com/"

    link = re.search(r'action="(Survey(.aspx\?c=[0-9][0-9][0-9][0-9][0-9][0-9]))"', s)

    link = link.group(1)

    url = mcd + link

    return url


# from https://stackoverflow.com/questions/49253246/how-to-close-requests-session
'''A function that clears the session'''
def close(self):

    # i guess closes all the adapters
    for v in self.adapters.values():
        v.close()


# if program run primarily, call main
if __name__ == "__main__":
    main()