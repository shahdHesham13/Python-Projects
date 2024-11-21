## Beautiful soup fundamentals

 ### *Contains*:

### i. **Set-up and Workflow**

 First a structured approach to web scraping by understanding the complete workflow.           
#### **The Workflow of Web Scraping**
1. **Inspect the page code to identify data and tools needed.**
2. **Make a request to the server** to retrieve the HTML code of the page.
3. **Parse the HTML** into a structured form using a suitable parser.
4. **Create a BeautifulSoup object** for navigation and data extraction.
5. **Export the HTML code to a file** for further inspection (optional).



#### **Step-by-Step Explanation**
#### 1. **Inspect the Webpage Code**
- Inspect the code of the webpage through the developer s tool in our browser to give us a general idea of how the page is structured and where the data may be located.<br>
NOTE: the developer code usually runs the JavaScript code that changes the HTML, so the HTML which we usually get when we scrape may be substantially different.

#### 2. **Make a Request**
- Similar to the calls of APIs, as in making `GET` request using `requests` library
the HTML now will be returned as response as one ling text so in step 3.....

#### 3. **Parse the HTML**
- Manipulating it as a huge string is inconvenient so we will approach it in a different way that is Parsing.
Parsing is splitting a string or text into syntactical components that can then be more easily processed.
in this case Parsing will be identifying all the elements, their relationships to one another, their attributes and contents this will be represented through parse tree.
- We have three options for the parser:
  - `html.parser` (Inbuild Python parser) (the worst).
  - `LXML` (faster).
  - `html5lib` (slowest) (most consistent).

#### 4. **Process the Parse Tree**
-  Processing the tree to extract the information we want, here we using the Beautiful soup package which provide a clean interface for navigation and searching, as we pass the HTML string and the parser to a constructor to create object.

#### 5. **Export the HTML to a File**
- Optional but recommended to save the raw HTML.
- Because the code in the browser may be different from the one sent to us, also the parser may have not parsed it correctly.


### ii. **Searching and Navigating the HTML Tree**  
   - Techniques to explore and understand the structure of a webpage.  
   - Parsing tools and navigate HTML elements.  

### iii. **Extracting Data from the HTML Tree**  
   - Locating specific data in HTML using tags, attributes, and classes, extracting and cleaning the desired information.  

### iv. **Practical Examples**  
   - with links relative absolute  
   - Processing Multiple Links  
   

### v. **Extracting Data from Nested Tags**  

### vi. **Scraping Multiple Pages Automatically**  
   - Automating the process of navigating and extracting information from multiple pages that by connecting alot of pages in a small amount of time and then extract only the information you need.
   - The objective is to get only all the useful text from those wikipedia pages
<ul>
<li> We will do that by extracting all text contained in a paragraph element,
<li> for all paragraphs on a page,
<li> for all pages (in note_urls)