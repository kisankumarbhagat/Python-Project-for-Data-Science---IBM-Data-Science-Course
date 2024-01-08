# Question 1: Use yfinance to Extract Stock Data
# Step 1: Create a ticker object for Tesla (TSLA)
tesla_ticker = yf.Ticker("TSLA")

# Step 2: Extract stock information and save it in a dataframe named tesla_data
tesla_data = tesla_ticker.history(period="max")

# Step 3: Reset the index
tesla_data.reset_index(inplace=True)

# Step 4: Save the dataframe (optional)
# tesla_data.to_csv('tesla_stock_data.csv')

# Step 5: Display the first five rows
print(tesla_data.head())

# Question 2: Use Webscraping to Extract Tesla Revenue Data
# Step 1: Download the webpage
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text

# Step 2: Parse the html data using beautiful_soup
soup = BeautifulSoup(html_data, 'html.parser')

# Step 3: Extract the table with Tesla Revenue and store it in a dataframe named tesla_revenue
tesla_revenue = pd.read_html(str(soup.find_all("tbody")[1]))[0]

# Step 4: Clean the Revenue column
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace(',', '').str.replace('$', '')

# Step 5: Remove null or empty strings in the Revenue column
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

# Step 6: Display the last 5 rows of the tesla_revenue dataframe
print(tesla_revenue.tail())

# Question 3: Use yfinance to Extract Stock Data
# Step 1: Create a ticker object for GameStop (GME)
gme_ticker = yf.Ticker("GME")

# Step 2: Extract stock information and save it in a dataframe named gme_data
gme_data = gme_ticker.history(period="max")

# Step 3: Reset the index
gme_data.reset_index(inplace=True)

# Step 4: Save the dataframe (optional)
# gme_data.to_csv('gme_stock_data.csv')

# Step 5: Display the first five rows
print(gme_data.head())

# Question 4: Use Webscraping to Extract GME Revenue Data
# Step 1: Download the webpage
gme_url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
gme_html_data = requests.get(gme_url).text

# Step 2: Parse the html data using beautiful_soup
gme_soup = BeautifulSoup(gme_html_data, 'html.parser')

# Step 3: Extract the table with GME Revenue and store it in a dataframe named gme_revenue
gme_revenue = pd.read_html(str(gme_soup.find_all("table")[0]))[1]

# Step 4: Clean the Revenue column
gme_revenue['Revenue'] = gme_revenue['Revenue'].str.replace('$', '').str.replace(',', '')

# Step 5: Remove null or empty strings in the Revenue column
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
gme_revenue.dropna(inplace=True)

# Step 6: Display the last 5 rows of the gme_revenue dataframe
print(gme_revenue.tail())

# Question 5: Plot Tesla Stock Graph
# Step 1: Use the make_graph function to graph the Tesla Stock Data
make_graph(tesla_data, tesla_revenue, "Tesla (TSLA)")

# Question 6: Plot GameStop Stock Graph
# Step 1: Define a ticker object for GameStop (GME)
gme_ticker = yf.Ticker("GME")

# Step 2: Extract stock information and save it in a dataframe named gme_data
gme_data = gme_ticker.history(period="max")

# Step 3: Reset the index
gme_data.reset_index(inplace=True)

# Step 4: Use the make_graph function to plot the GameStop Stock Data
make_graph(gme_data, gme_revenue, "GameStop (GME)")
