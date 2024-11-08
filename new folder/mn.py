import requests
from bs4 import BeautifulSoup
import numpy as np

# Function to extract links from a URL
def get_links(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Ensure the link is a full URL (you may need to handle relative URLs as well)
            if href.startswith('http'):
                links.append(href)
        return links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

# Function to build the adjacency matrix from a list of URLs
def build_adjacency_matrix(urls):
    num_pages = len(urls)
    M = np.zeros((num_pages, num_pages))

    # For each URL, extract its links and update the adjacency matrix
    for i, url in enumerate(urls):
        links = get_links(url)
        print(links)
        for link in links:
            if link in urls:  # Only consider links between the given set of URLs
                j = urls.index(link)
                M[i, j] = 1  # Mark that URL i links to URL j

    return M


def page_rank(adjacency_matrix, num_iterations=100, d=0.85):
    """
    Computes PageRank of a graph represented by an adjacency matrix.

    Parameters:
        adj_matrix (np.array): Adjacency matrix of the graph.
        num_iterations (int): Number of iterations for the power method.
        d (float): Damping factor (usually 0.85).

    Returns:
        np.array: PageRank vector.
    """
    num_pages = adjacency_matrix.shape[0]

    # Normalize the adjacency matrix
    column_sums = np.sum(adjacency_matrix, axis=0)
    # Replace zero sums with one to avoid division by zero
    column_sums[column_sums == 0] = 1
    stochastic_matrix = adjacency_matrix / column_sums
    print(stochastic_matrix)

    # Initialize the PageRank vector
    page_rank = np.ones(num_pages) / num_pages
    print(page_rank)

    # Create the transition matrix with damping factor
    transition_matrix = d * stochastic_matrix + (1 - d) / num_pages * np.ones((num_pages, num_pages))
    print(transition_matrix)

    # Power iteration to find the steady state
    for _ in range(num_iterations):
        page_rank = np.dot(transition_matrix, page_rank)

    return page_rank

# List of URLs (replace with actual URLs or test URLs if available)
urls = [
    "http://127.0.0.1:5500/page1.html",
    "http://127.0.0.1:5500/page2.html",
    "http://127.0.0.1:5500/page3.html"
    
]

# Generate the adjacency matrix
adjacency_matrix = build_adjacency_matrix(urls)
print("Adjacency Matrix:")
print(adjacency_matrix)
pagerank_vector = page_rank(adjacency_matrix)
print("PageRank Vector:")
print(pagerank_vector)
