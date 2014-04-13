from moviebrowser import MovieBrowser

browser = MovieBrowser()

def check_database_exists():
    return (hasattr(browser, 'database_exists') and
            (browser.database_exists != False))

def init_browser():
    print "Checking if database exists"
    if check_database_exists():
        print "Database exists"
    else:
        print "Creating database"
        browser.init_database()

def list_available_genres():
    browser.list_available_genres()

if __name__=="__main__":
    init_browser()
    list_available_genres()