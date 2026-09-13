import re

# ============================================================
# BASIC INFORMATION RETRIEVAL SYSTEM
# ============================================================
# Features:
# 1. Document Collection
# 2. Text Preprocessing
# 3. Tokenization
# 4. Dictionary Creation
# 5. Inverted Index
# 6. Boolean AND
# 7. Boolean OR
# 8. Boolean NOT
# 9. User Query
# ============================================================


# ------------------------------------------------------------
# 1. DOCUMENT COLLECTION
# ------------------------------------------------------------

documents = {
    1: "Python is a programming language used for data science.",
    
    2: "Data science uses Python for machine learning.",
    
    3: "Machine learning is an important field of artificial intelligence.",
    
    4: "Information retrieval helps users search documents efficiently.",
    
    5: "Python can be used to build information retrieval systems."
}


# ------------------------------------------------------------
# 2. PREPROCESSING FUNCTION
# ------------------------------------------------------------

def preprocess(text):
    """
    Converts text to lowercase and removes
    special characters and punctuation.
    """

    # Convert text to lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r'[^a-z0-9\s]', '', text)

    return text


# ------------------------------------------------------------
# 3. TOKENIZATION FUNCTION
# ------------------------------------------------------------

def tokenize(text):
    """
    Converts a document into individual words/tokens.
    """

    text = preprocess(text)

    # Split text into words
    tokens = text.split()

    return tokens


# ------------------------------------------------------------
# 4. CREATE DICTIONARY
# ------------------------------------------------------------

dictionary = set()

for doc_id, text in documents.items():

    # Tokenize each document
    tokens = tokenize(text)

    # Add tokens to dictionary
    dictionary.update(tokens)


# Convert set to sorted list
dictionary = sorted(dictionary)


# ------------------------------------------------------------
# 5. CREATE INVERTED INDEX
# ------------------------------------------------------------

inverted_index = {}

for doc_id, text in documents.items():

    # Get tokens from the document
    tokens = tokenize(text)

    for token in tokens:

        # If the word does not exist in index,
        # create an empty set
        if token not in inverted_index:
            inverted_index[token] = set()

        # Add document ID to the term's postings list
        inverted_index[token].add(doc_id)


# ------------------------------------------------------------
# 6. BOOLEAN AND FUNCTION
# ------------------------------------------------------------

def boolean_and(term1, term2):

    """
    Returns documents containing BOTH terms.
    """

    # Convert terms to lowercase
    term1 = term1.lower()
    term2 = term2.lower()

    # Get postings lists
    list1 = inverted_index.get(term1, set())
    list2 = inverted_index.get(term2, set())

    # Intersection gives AND result
    result = list1 & list2

    return sorted(result)


# ------------------------------------------------------------
# 7. BOOLEAN OR FUNCTION
# ------------------------------------------------------------

def boolean_or(term1, term2):

    """
    Returns documents containing AT LEAST ONE
    of the two terms.
    """

    # Convert terms to lowercase
    term1 = term1.lower()
    term2 = term2.lower()

    # Get postings lists
    list1 = inverted_index.get(term1, set())
    list2 = inverted_index.get(term2, set())

    # Union gives OR result
    result = list1 | list2

    return sorted(result)


# ------------------------------------------------------------
# 8. BOOLEAN NOT FUNCTION
# ------------------------------------------------------------

def boolean_not(term):

    """
    Returns documents that DO NOT contain the term.
    """

    # Convert term to lowercase
    term = term.lower()

    # Get all document IDs
    all_documents = set(documents.keys())

    # Get documents containing the term
    term_documents = inverted_index.get(term, set())

    # Difference gives NOT result
    result = all_documents - term_documents

    return sorted(result)


# ------------------------------------------------------------
# 9. DISPLAY DOCUMENTS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("           INFORMATION RETRIEVAL SYSTEM")
print("=" * 60)

print("\n1. DOCUMENT COLLECTION")
print("-" * 60)

for doc_id, text in documents.items():
    print(f"Document {doc_id}: {text}")


# ------------------------------------------------------------
# 10. DISPLAY TOKENIZED DOCUMENTS
# ------------------------------------------------------------

print("\n2. TOKENIZED DOCUMENTS")
print("-" * 60)

for doc_id, text in documents.items():

    tokens = tokenize(text)

    print(f"Document {doc_id}:")
    print(tokens)


# ------------------------------------------------------------
# 11. DISPLAY DICTIONARY
# ------------------------------------------------------------

print("\n3. DICTIONARY")
print("-" * 60)

print(f"Total unique terms: {len(dictionary)}")

print("\nTerms:")

for word in dictionary:
    print(word)


# ------------------------------------------------------------
# 12. DISPLAY INVERTED INDEX
# ------------------------------------------------------------

print("\n4. INVERTED INDEX")
print("-" * 60)

for term in sorted(inverted_index):

    # Convert set to sorted list
    doc_list = sorted(inverted_index[term])

    print(f"{term:15} -> {doc_list}")


# ------------------------------------------------------------
# 13. BOOLEAN RETRIEVAL EXAMPLES
# ------------------------------------------------------------

print("\n5. BOOLEAN RETRIEVAL")
print("-" * 60)


# AND example
result_and = boolean_and("python", "data")

print("\nQuery: python AND data")
print("Result:", result_and)


# OR example
result_or = boolean_or("python", "machine")

print("\nQuery: python OR machine")
print("Result:", result_or)


# NOT example
result_not = boolean_not("python")

print("\nQuery: NOT python")
print("Result:", result_not)


# ------------------------------------------------------------
# 14. DISPLAY ACTUAL DOCUMENTS FOR RESULTS
# ------------------------------------------------------------

print("\n6. DOCUMENTS RETRIEVED")
print("-" * 60)

print("\nFor query: python AND data")

result = boolean_and("python", "data")

if result:
    for doc_id in result:
        print(f"Document {doc_id}: {documents[doc_id]}")
else:
    print("No documents found.")


print("\nFor query: python OR machine")

result = boolean_or("python", "machine")

if result:
    for doc_id in result:
        print(f"Document {doc_id}: {documents[doc_id]}")
else:
    print("No documents found.")


print("\nFor query: NOT python")

result = boolean_not("python")

if result:
    for doc_id in result:
        print(f"Document {doc_id}: {documents[doc_id]}")
else:
    print("No documents found.")


# ------------------------------------------------------------
# 15. INTERACTIVE SEARCH
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("             INTERACTIVE BOOLEAN SEARCH")
print("=" * 60)

print("\nAvailable operators:")
print("AND")
print("OR")
print("NOT")

print("\nExamples:")
print("python AND data")
print("python OR machine")
print("NOT python")

query = input("\nEnter your Boolean query: ")

# Convert query to lowercase
query = query.lower().strip()


# ------------------------------------------------------------
# 16. PROCESS USER QUERY
# ------------------------------------------------------------

if " and " in query:

    # Split query into two terms
    parts = query.split(" and ")

    if len(parts) == 2:

        term1 = parts[0].strip()
        term2 = parts[1].strip()

        result = boolean_and(term1, term2)

        print("\nQuery Type: AND")
        print("Search Terms:", term1, "AND", term2)

    else:
        result = []

        print("\nInvalid AND query.")


elif " or " in query:

    # Split query into two terms
    parts = query.split(" or ")

    if len(parts) == 2:

        term1 = parts[0].strip()
        term2 = parts[1].strip()

        result = boolean_or(term1, term2)

        print("\nQuery Type: OR")
        print("Search Terms:", term1, "OR", term2)

    else:
        result = []

        print("\nInvalid OR query.")


elif query.startswith("not "):

    # Get term after NOT
    term = query[4:].strip()

    result = boolean_not(term)

    print("\nQuery Type: NOT")
    print("Search Term:", term)


else:

    # Simple single-term search
    term = query.strip()

    result = sorted(inverted_index.get(term, set()))

    print("\nQuery Type: Single Term")
    print("Search Term:", term)


# ------------------------------------------------------------
# 17. DISPLAY SEARCH RESULTS
# ------------------------------------------------------------

print("\n" + "-" * 60)
print("SEARCH RESULTS")
print("-" * 60)

if result:

    print(f"Found {len(result)} matching document(s).\n")

    for doc_id in result:

        print(f"Document {doc_id}:")
        print(documents[doc_id])
        print()

else:

    print("No matching documents found.")


# ------------------------------------------------------------
# 18. PROGRAM FINISHED
# ------------------------------------------------------------

print("=" * 60)
print("       INFORMATION RETRIEVAL SYSTEM FINISHED")
print("=" * 60)