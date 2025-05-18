<!DOCTYPE html>
</head>
<body>
  <h1>Laptop Data Analytics Pipeline with Python, SQL, and Web Scraping</h1>
  
  <p>This project demonstrates a full <strong>data analytics pipeline</strong> — from <strong>web scraping laptop listings on Amazon</strong>, to <strong>transforming raw HTML into structured data</strong>, and finally <strong>loading it into a MySQL database</strong> for powerful querying and analysis.</p>
  
  <p>It enables analysts to explore laptop pricing, performance, storage capacity, and other specifications to derive actionable insights or make data-driven recommendations.</p>
  
  <h2>Objective</h2>
  
  <p>To build a structured dataset of laptops scraped from Amazon and use it for <strong>exploratory analysis</strong>, <strong>trend identification</strong>, and <strong>user-driven querying</strong> using SQL. The cleaned data is suitable for further visualization or dashboard development (e.g., in Tableau or Power BI).</p>
  
  <table>
    <thead>
      <tr>
        <th>Component</th>
        <th>Tool/Library</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Web Scraping</td>
        <td><code>Selenium</code>, <code>BeautifulSoup</code></td>
      </tr>
      <tr>
        <td>Data Wrangling</td>
        <td><code>pandas</code></td>
      </tr>
      <tr>
        <td>Database</td>
        <td><code>MySQL</code></td>
      </tr>
      <tr>
        <td>Language</td>
        <td><code>Python</code></td>
      </tr>
      <tr>
        <td>Analytics</td>
        <td>SQL Queries, Tableau-ready</td>
      </tr>
    </tbody>
  </table>
  
  <h2>Project Workflow</h2>
  
  <pre><code>├── data/ # Raw HTML blocks saved from Amazon
├── data_extract.py # Scrapes product data using Selenium
├── transform.py # Extracts features from HTML using BeautifulSoup
├── load.py # Cleans and inserts data into MySQL
├── laptop.csv # Output file for structured and cleaned data
├── README.md # Documentation</code></pre>
  
  <h2>Data Analytics Use Cases</h2>
  
  <p>After loading the dataset into MySQL, data analysts can:</p>
  
  <ul>
    <li>🔍 Filter laptops by specs (RAM, storage, rating, price)</li>
    <li>💰 Compare price-to-performance or price-per-GB metrics</li>
    <li>🏆 Rank laptops based on rating and value</li>
    <li>📊 Visualize market trends, brand offerings, or price distribution</li>
  </ul>
  
  <h2>🛠 How to Run</h2>
  
  <ol start="2">
    <li>
      <p>Set Up MySQL</p>
      <p>Create the database amazon and configure your credentials in load.py:</p>
      <pre><code class="language-sql">CREATE DATABASE amazon;</code></pre>
    </li>
    <li>
      <p>Run Each Step</p>
      <ul>
        <li><code>data_extract.py</code>: Scrapes laptops from Amazon and stores as HTML files.</li>
        <li><code>transform.py</code>: Parses HTML and saves structured data to laptop.csv.</li>
        <li><code>load.py</code>: Cleans data and loads it into MySQL.</li>
      </ul>
    </li>
  </ol>
  
  <h2>Sample Analytics Queries</h2>
  
  <ol>
    <li>
      <p>Find Best Value Laptops (Price Per GB)</p>
      <pre><code class="language-sql">SELECT title, price, disk_size, ROUND(price / disk_size, 2) AS price_per_gb
FROM laptop
WHERE disk_size > 0 AND price > 0
ORDER BY price_per_gb ASC
LIMIT 10;</code></pre>
    </li>
    <li>
      <p>Retrieve Laptops by User Requirement</p>
      <pre><code class="language-sql">SELECT * FROM laptop
WHERE ram >= 8 AND disk_size >= 512 AND rating >= 4
AND price <= 1000
ORDER BY rating DESC;</code></pre>
    </li>
  </ol>
  
  <h2>Sample Fields Available</h2>
  <ul>
    <li><code>title</code></li>
    <li><code>price</code> (float)</li>
    <li><code>rating</code> (float)</li>
    <li><code>disk_size</code> (in GB)</li>
    <li><code>ram</code> (in GB)</li>
    <li><code>link</code> (to view product)</li>
  </ul>
</body>
</html>
