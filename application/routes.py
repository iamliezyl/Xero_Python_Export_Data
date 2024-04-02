#import app object from __init__.py
from application import app 
from flask import render_template, redirect, request
import base64
import json
import webbrowser
import sys
import pyperclip
import time
import keyboard
import pygetwindow as gw
import pyautogui
import requests
from application.exportUtilities import *



@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",  index = True )

@app.route("/utilities")
def utilities():
    return render_template("utilities.html",  utilities = True )


@app.route("/xero_backup")
def xero_backup():
    old_tokens = XeroFirstAuth()
    XeroRefreshToken(old_tokens[1])
    XeroRequests()

    return("TRUE")

client_id = 'F845C78C95A84CB494734CB86AE88201'
client_secret = 'Qc5M9ItNpRgU2iyMln5qSERxxyvEw0amPpFyo2r52nzACPBH'
redirect_url = 'http://localhost:5000/callback/'
scope = 'offline_access accounting.transactions accounting.settings.read accounting.budgets.read accounting.contacts'
b64_id_secret = base64.b64encode(bytes(client_id + ':' + client_secret, 'utf-8')).decode('utf-8')
 
def XeroFirstAuth():    
# 1. Send a user to authorize your app

      
    auth_url = ('''https://login.xero.com/identity/connect/authorize?'''+
                '''response_type=code''' +
                '''&client_id=''' + client_id +
                '''&redirect_uri=''' + redirect_url +
                '''&scope=''' + scope +
                '''&state=123''')
    webbrowser.open_new(auth_url)
        
     # 2. Users are redirected back to you with a code
    auth_res_url = input('What is the response URL? ')
    start_number = auth_res_url.find('code=') + len('code=')
    end_number = auth_res_url.find('&scope')
    auth_code = auth_res_url[start_number:end_number]
    
    print("auth code: " + auth_code, file=sys.stdout)
    print('\n')

    exchange_code_url = 'https://identity.xero.com/connect/token'
    response = requests.post(exchange_code_url, 
                            headers = {
                                'Authorization': 'Basic ' + b64_id_secret
                            },
                            data = {
                                'grant_type': 'authorization_code',
                                'code': auth_code,
                                'redirect_uri': redirect_url
                            })
    json_response = response.json()
    print("...")
    print(json_response)
    print('\n')
    
     # 4. Receive your tokens
    return [json_response['access_token'], json_response['refresh_token']]

    # 5. Check the full set of tenants you've been authorized to access
def XeroTenants(access_token):
    connections_url = 'https://api.xero.com/connections'
    response = requests.get(connections_url,
                           headers = {
                               'Authorization': 'Bearer ' + str(access_token),
                               'Content-Type': 'application/json'
                           })
    json_response = response.json()
    print("xero tenants json response: " + str(len(json_response)))
    print(json_response)
    json_dict = []
    for tenants in json_response:
        json_dict = tenants
        #print(json_dict[0])
    return json_dict

#XeroTenants('YOUR_XERO_ACCESS_TOKEN')  // to restore
    

# 6.1 Refreshing access tokens
def XeroRefreshToken(refresh_token):
    token_refresh_url = 'https://identity.xero.com/connect/token'
    response = requests.post(token_refresh_url,
                            headers = {
                                'Authorization' : 'Basic ' + b64_id_secret,
                                'Content-Type': 'application/x-www-form-urlencoded'
                            },
                            data = {
                                'grant_type' : 'refresh_token',
                                'refresh_token' : refresh_token
                            })
    json_response = response.json()
    print("Xero Refresh token reponse: ")
    print(json_response)
    
    new_refresh_token = json_response['refresh_token']
    rt_file = open(r'C:/folder/refresh_token.txt', 'w')
    rt_file.write(new_refresh_token)
    rt_file.close()
    
    return [json_response['access_token'], json_response['refresh_token']]

# 6.2 Call the API
def XeroRequests():

    print("XeroRequests")
    old_refresh_token = open(r'C:/folder/refresh_token.txt', 'r').read()
    new_tokens = XeroRefreshToken(old_refresh_token)
    xero_tenant_id = XeroTenants(new_tokens[0])

    exportBankTransactions(xero_tenant_id, new_tokens)
    exportBankTransfers(xero_tenant_id, new_tokens)
    exportBatchPayments(xero_tenant_id, new_tokens)
    exportBrandingThemes(xero_tenant_id, new_tokens)
    exportBudgets(xero_tenant_id, new_tokens)
    exportContactGroups(xero_tenant_id, new_tokens)
    exportContacts(xero_tenant_id, new_tokens)
    exportCreditNotes(xero_tenant_id, new_tokens)
    exportCurrencies(xero_tenant_id, new_tokens)
    exportEmployees(xero_tenant_id, new_tokens)
    exportExpenseClaims(xero_tenant_id, new_tokens)
    exportInvoices(xero_tenant_id, new_tokens)
    exportInvoiceReminders(xero_tenant_id, new_tokens)
    exportItems(xero_tenant_id, new_tokens)
    exportJournals(xero_tenant_id, new_tokens)
    exportLinkedTransactions(xero_tenant_id, new_tokens)
    exportManualJournals(xero_tenant_id, new_tokens)
    exportOrganisationActions(xero_tenant_id, new_tokens)
    exportOrganisation(xero_tenant_id, new_tokens)
    exportOverpayments(xero_tenant_id, new_tokens)
    exportPayments(xero_tenant_id, new_tokens)
    exportPrepayments(xero_tenant_id, new_tokens) #nocontent
    exportPurchaseOrders(xero_tenant_id, new_tokens) #nocontent
    exportQuotes(xero_tenant_id, new_tokens) #fewContentUnused
    exportReceipts(xero_tenant_id, new_tokens) #nocontent
    exportRepeatingInvoices(xero_tenant_id, new_tokens) #fewContentUnused
    exportTaxRates(xero_tenant_id, new_tokens)
    exportTrackingCategories(xero_tenant_id, new_tokens) #nocontent
    exportUsers(xero_tenant_id, new_tokens)


def export_csv():
    invoices = open('C:/folder/xero_output.txt', 'r').read()
    json_invoice = json.loads(invoices)
    analysis = open(r'C:/folder/analysis.csv', 'w')
    analysis.write('Type' + ',' + 'Total')
    analysis.write('\n')
    for invoices in json_invoice['Invoices']:
        analysis.write(invoices['Type'] + ',' + str(invoices['Total']))
        analysis.write('\n')
    analysis.close()

import pandas as pd
import matplotlib.pyplot as plt
def chart_data():
    df = pd.read_csv(r'C:\folder\analysis.csv')
    pvt = df[ ['Type','Total'] ].groupby('Type').sum()
    print(pvt)
    
    pvt.plot.bar(stacked=True)
    plt.show()


#export_csv()
#chart_data()

# First Time running the script
# old_tokens = XeroFirstAuth()
#print("old token: " + old_tokens[1])
#XeroRefreshToken(old_tokens[1])

# Every other time

