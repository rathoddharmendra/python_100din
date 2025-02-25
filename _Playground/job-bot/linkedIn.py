from beautifulSoup import bs4

class LinkedIn:
    def __init__(self, driver):
        self.driver = driver
        self.bs = bs4()

    def login(self, username, password):
        self.driver.get('https://www.linkedin.com/login')
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_class_name('btn__)'
        'primary--large').click()

    def search(self, query):
        self.driver.get('https://www.linkedin.com/search/results/all/?keywords=' + query)
        self.bs.set_soup(self.driver.page_source)
        results = self.bs.get_elements('div', 'search-result__info')
        for result in results:
            name = self.bs.get_element('span', 'name actor-name').text
            title = self.bs.get_element('p', 'subline-level-1').text
            location = self.bs.get_element('p', 'subline-level-2').text
            print(name, title, location)

    def connect(self, query):
        self.search(query)
        results = self.bs.get_elements('button', 'search-result__action-button')
        for result in results:
            if result.text == 'Connect':
                result.click()
                self.driver.find_element_by_class_name('ml1').click()   
                break

    def message(self, query, message):
        self.search(query)
        results = self.bs.get_elements('button', 'search-result__action-button')
        for result in results:
            if result.text == 'Message':
                result.click()
                self.driver.find_element_by_class_name('msg-form__contenteditable').send_keys(message)
                self.driver.find_element_by_class_name('msg-form__send-button').click()
                break

    def visit(self, query):

        self.search(query)
        results = self.bs.get_elements('a', 'search-result__result-link')
        for result in results:
            result.click()
            break


        