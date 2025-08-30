# coding: utf-8
import pandas as pd
import os

# Load the TSV file
publications = pd.read_csv("publications.tsv", sep="\t", header=0)

# HTML escape function
html_escape_table = {
    "&": "&amp;",
    "\"": "&quot;",
    "'": "&apos;"
}
def html_escape(text):
    if not isinstance(text, str):
        return text
    return "".join(html_escape_table.get(c,c) for c in text)

# Loop through publications and generate markdown files
for row, item in publications.iterrows():
    md_filename = str(item.pub_date) + "-" + item.url_slug + ".md"
    html_filename = str(item.pub_date) + "-" + item.url_slug
    year = item.pub_date[:4]

    # Determine category based on venue
    venue_lower = str(item.venue).lower()
    category = 'manuscripts' # Default category
    if 'conference' in venue_lower or 'workshop' in venue_lower or 'proceedings' in venue_lower:
        category = 'conferences'
    elif 'book' in venue_lower:
        category = 'books'

    ## YAML variables
    md = "---"
    md += "\ntitle: \""   + html_escape(item.title) + '\"\n'
    md += "collection: publications" + "\n"
    md += "permalink: /publication/" + html_filename + "\n"
    
    if len(str(item.excerpt)) > 5:
        md += "excerpt: '" + html_escape(item.excerpt) + "'\n"
    
    md += "date: " + str(item.pub_date) + "\n"
    md += "venue: '" + html_escape(item.venue) + "'\n"
    md += "category: '" + category + "'\n" # Add category here

    if len(str(item.paper_url)) > 5:
        md += "paperurl: '" + item.paper_url + "'\n"
    
    md += "citation: '" + html_escape(item.citation) + "'\n"
    md += "---"
    
    ## Markdown description for individual page
     
        
    if len(str(item.excerpt)) > 5:
        md += "\n" + html_escape(item.excerpt) + "\n"
        
    md += "\nRecommended citation: " + html_escape(item.citation)
    
    md_filename = os.path.basename(md_filename)
       
    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md)