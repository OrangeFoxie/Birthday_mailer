def googleSetup():
    service_account_file = '.\keyAPI\getUserBirthday\service.json'
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    sample_spreadsheet_id = '1gINjp6tlqbd2XN2jgWjlQ-qKTKo3K8LIDJHjwIkpX1I'
    sample_range_name = 'BirthDay!A2:D'
    return {
        'service_account_file':service_account_file,
        'scopes':scope,
        'sample_spreadsheet_id':sample_spreadsheet_id,
        'sample_range_name':sample_range_name
    }