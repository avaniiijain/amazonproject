# 1. IMPORT LIBRARIES
import pandas as pd
import mysql.connector
from mysql.connector import Error

# 2. LOAD DATA
def load_data():
    """Load the laptop dataset from CSV file"""
    df = pd.read_csv("C:\\Users\\avani\\OneDrive\\Documents\\Python_Final_Project\\laptop.csv")
    print(f"Loaded {len(df)} laptop records")
    return df

# 3. DATA CLEANING FUNCTIONS
def clean_price(price):
    """
    Cleans the price column by removing '$' and ',' and converting to float.
    Handles both string and float/int inputs.
    """
    try:
        if isinstance(price, str):
            return float(price.replace('$', '').replace(',', ''))
        elif isinstance(price, (float, int)):
            return float(price)
        else:
            return 0.0
    except Exception:
        return 0.0

def clean_storage_value(value):
    """
    Converts storage size strings into numeric values in GB.
    Example: '1TB' becomes 1024, '500GB' remains 500.
    """
    try:
        value = str(value).lower()
        if 'tb' in value:
            return float(value.replace('tb', '').strip()) * 1024  # Convert TB to GB
        return float(value.replace('gb', '').strip())
    except (ValueError, AttributeError):
        return 0.0  # Return default value instead of None

def clean_ram_value(value):
    """
    Converts RAM size strings into numeric values in GB.
    Example: '8GB' becomes 8.0, '16 GB' becomes 16.0
    """
    try:
        value = str(value).lower()
        if 'gb' in value:
            return float(value.replace('gb', '').strip())
        elif 'mb' in value:
            return float(value.replace('mb', '').strip()) / 1024  # Convert MB to GB
        elif 'tb' in value:
            return float(value.replace('tb', '').strip()) * 1024  # Convert TB to GB
        return float(value)
    except (ValueError, AttributeError):
        return 0.0  # Return default value instead of None

# 4. CLEAN AND PREPARE DATA
def clean_data(df):
    """Apply all cleaning functions to the dataframe"""
    # Clean price values
    df['price'] = df['price'].apply(clean_price)
    
    # Clean disk_size values
    df['disk_size'] = df['disk_size'].apply(clean_storage_value)
    
    # Clean RAM values
    df['ram'] = df['ram'].apply(clean_ram_value)
    
    # Fill any remaining NaN values with 0
    df = df.fillna(0)
    
    return df

# 5. DATABASE FUNCTIONS
def create_connection(host_name, user_name, user_password, db_name):
    """Create a connection to MySQL database"""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    
    return connection

def execute_query(connection, query):
    """Execute a SQL query"""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_into_table(connection, df):
    """Insert DataFrame data into MySQL table"""
    cursor = connection.cursor()
    count = 0
    
    # Ensure the dataframe has no NaN values
    df = df.fillna(0)
    
    try:
        for i, row in df.iterrows():
            sql = "INSERT INTO laptop (title, price, rating, disk_size, ram, link) VALUES (%s, %s, %s, %s, %s, %s)"
            # Convert all values to appropriate types
            values = (
                str(row['title']), 
                float(row['price']), 
                float(row['rating']), 
                float(row['disk_size']), 
                float(row['ram']),  # Ensure ram is float, not NaN
                str(row['link'])
            )
            cursor.execute(sql, values)
            count += 1
        connection.commit()
        print(f"Data inserted successfully: {count} records")
    except Error as e:
        print(f"Error: {e}")

# 6. DATABASE SETUP FUNCTIONS
def setup_database(connection):
    """Create and configure the database tables"""
    # Update the ram column to FLOAT instead of VARCHAR to match our data
    create_laptop_table = """
    CREATE TABLE IF NOT EXISTS laptop (
        id INT AUTO_INCREMENT, 
        title VARCHAR(255) NOT NULL,
        price FLOAT NOT NULL,
        rating FLOAT NOT NULL,
        disk_size FLOAT NOT NULL,
        ram FLOAT NOT NULL,
        link VARCHAR(2048) NOT NULL,
        PRIMARY KEY (id)
    ) ENGINE = InnoDB
    """
    execute_query(connection, create_laptop_table)

# 7. MAIN EXECUTION FUNCTION
def main():
    # Load the data
    df = load_data()
    print("Data preview:")
    print(df.head(3))
    
    # Clean the data
    df = clean_data(df)
    print("\nData info after cleaning:")
    print(df.info())
    
    # Connect to database
    connection = create_connection("127.0.0.1", "root", "Ammu$2020", "amazon")
    
    # Setup database schema
    setup_database(connection)
    
    # Insert data into the database
    insert_into_table(connection, df)
    
    # Close connection
    connection.close()
    print("Database connection closed")

# Execute the main function
if __name__ == "__main__":
    main()