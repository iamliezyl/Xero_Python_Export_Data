import requests

def exportInvoices(xero_tenant_id, new_tokens):

    get_url = 'https://api.xero.com/api.xro/2.0/Invoices'
    xero_output = open(r'C:/folder/xero_invoices.txt', 'w', encoding="utf-8")    
    getData(get_url, new_tokens, xero_tenant_id, xero_output)
    

def exportItems(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/Items'
    xero_output = open(r'C:/folder/xero_items.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportBankTransactions(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/BankTransactions'
    xero_output = open(r'C:/folder/xero_bank_transactions.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportBankTransfers(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/BankTransfers'
    xero_output = open(r'C:/folder/xero_bank_transfers.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportBatchPayments(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/BatchPayments'
    xero_output = open(r'C:/folder/xero_batch_payments.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportBrandingThemes(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/BrandingThemes'
    xero_output = open(r'C:/folder/xero_branding_themes.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportBudgets(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/Budgets'
    xero_output = open(r'C:/folder/xero_budgets.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportContactGroups(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/ContactGroups'
    xero_output = open(r'C:/folder/xero_ContactGroups.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportContacts(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/Contacts'
    xero_output = open(r'C:/folder/xero_Contacts.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportCreditNotes(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/CreditNotes'
    xero_output = open(r'C:/folder/xero_exportCreditNotes.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportCurrencies(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/Currencies'
    xero_output = open(r'C:/folder/xero_Currencies.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportEmployees(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/Employees'
    xero_output = open(r'C:/folder/xero_Employees.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportExpenseClaims(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/ExpenseClaims'
    xero_output = open(r'C:/folder/xero_ExpenseClaims.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportInvoiceReminders(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/InvoiceReminders/Settings'
    xero_output = open(r'C:/folder/xero_InvoiceReminders.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportJournals(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/Journals'
    xero_output = open(r'C:/folder/xero_Journals.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportLinkedTransactions(xero_tenant_id, new_tokens): #no content
    get_url = 'https://api.xero.com/api.xro/2.0/LinkedTransactions'
    xero_output = open(r'C:/folder/xero_LinkedTransactions.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportManualJournals(xero_tenant_id, new_tokens): 
    get_url = 'https://api.xero.com/api.xro/2.0/ManualJournals'
    xero_output = open(r'C:/folder/xero_ManualJournals.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportOrganisationActions(xero_tenant_id, new_tokens): 
    get_url = 'https://api.xero.com/api.xro/2.0/Organisation/Actions'
    xero_output = open(r'C:/folder/xero_OrganisationActions.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportOrganisation(xero_tenant_id, new_tokens): 
    get_url = 'https://api.xero.com/api.xro/2.0/Organisation'
    xero_output = open(r'C:/folder/xero_Organisation.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportOverpayments(xero_tenant_id, new_tokens): 
    get_url = 'https://api.xero.com/api.xro/2.0/Overpayments'
    xero_output = open(r'C:/folder/xero_Overpayments.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportPayments(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/Payments'
    xero_output = open(r'C:/folder/xero_Payments.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportPrepayments(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/Prepayments'
    xero_output = open(r'C:/folder/xero_Prepayments.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportPurchaseOrders(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/PurchaseOrders'
    xero_output = open(r'C:/folder/xero_PurchaseOrders.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportQuotes(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/Quotes'
    xero_output = open(r'C:/folder/xero_Quotes.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportReceipts(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/Receipts'
    xero_output = open(r'C:/folder/xero_Receipts.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportRepeatingInvoices(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/RepeatingInvoices'
    xero_output = open(r'C:/folder/xero_RepeatingInvoices.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportTaxRates(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/TaxRates'
    xero_output = open(r'C:/folder/xero_TaxRates.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportTrackingCategories(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/TrackingCategories'
    xero_output = open(r'C:/folder/xero_TrackingCategories.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)

def exportUsers(xero_tenant_id, new_tokens):
    get_url = 'https://api.xero.com/api.xro/2.0/Users'
    xero_output = open(r'C:/folder/xero_Users.txt', 'w', encoding="utf-8")
    getData(get_url, new_tokens, xero_tenant_id, xero_output)


def getData(getUrl, new_tokens, xero_tenant_id, xero_output):
    
    header_content = { "Authorization": "Bearer " + str(new_tokens[0]),
                    "Xero-tenant-id": xero_tenant_id.get('tenantId'),
                    "Accept": "application/json"
                    }
    response = requests.get(getUrl,
                           headers = header_content)
    json_response = response.json()
    
    #xero_output = open(r'C:/folder/xero_items.txt', 'w', encoding="utf-8")
    xero_output.write(response.text)
    xero_output.close()
