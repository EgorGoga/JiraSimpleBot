from jira import JIRA
import pandas as pd

login = "ezavodenko"
password = "Quqish89"
serv = "https://jira.fil-it.ru"
#Jira connect
jira_options = {'server': serv}
jira = JIRA(options=jira_options, basic_auth=(login, password))

team = [
    'Дорогавцев Дмитрий Алексеевич',
    'Мусаев Руслан Гаджимурадович',
    'Агафонов Денис Романович',
    'Миля Дмитрий Игоревич']

#Search jira issues
def jira_hist(sprint):
    jira_search = jira.search_issues(jql_str=f"project = 'GISMURP' AND Sprint = '{sprint}'", maxResults = 1000, expand='changelog')
    return jira_search

#Take issues history of assigne by users

def get_assignees(issue):
    assignees = []
    for history in issue.changelog.histories:
        for item in history.items:
            if item.field == 'assignee':
                assignees.append(item.fromString)
    assignees.append(issue.fields.assignee.displayName)
    return assignees

def right_version(jira_list):
    assignees_dict = {}
    for issue in jira_list:
        a = get_assignees(issue)
        for asignee in a:
            if asignee in team:
                assignees_dict[issue.key] = a
                break
    return assignees_dict

