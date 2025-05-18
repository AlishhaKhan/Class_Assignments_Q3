import streamlit as st
import os
import json

# ---------- FILE HANDLING ----------
LIBRARY_FILE = "library_data.txt"

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as f:
        json.dump(library, f, indent=2)

# ---------- SESSION INIT ----------
if "library" not in st.session_state:
    st.session_state.library = load_library()

# ---------- FUNCTIONS ----------
def format_book(book):
    status = "Read" if book["read"] else "Unread"
    return f"📖 {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}"

def display_all_books():
    if not st.session_state.library:
        st.info("Your library is empty.")
    else:
        for idx, book in enumerate(st.session_state.library, start=1):
            st.markdown(f"**{idx}.** {format_book(book)}")

def calculate_stats():
    total = len(st.session_state.library)
    if total == 0:
        return 0, 0.0
    read_count = sum(1 for book in st.session_state.library if book["read"])
    return total, (read_count / total) * 100

def remove_by_title(title):
    before = len(st.session_state.library)
    st.session_state.library = [b for b in st.session_state.library if b["title"].lower() != title.lower()]
    after = len(st.session_state.library)
    return before != after

def search_books(query, by):
    query = query.lower()
    if by == "Title":
        return [b for b in st.session_state.library if query in b["title"].lower()]
    else:
        return [b for b in st.session_state.library if query in b["author"].lower()]

# ---------- STREAMLIT UI ----------
st.set_page_config(page_title="📚 Personal Library Manager", layout="centered")
st.title("📚 Personal Library Manager")

menu = st.sidebar.radio("📌 Menu", [
    "Add a Book", 
    "Remove a Book", 
    "Search for a Book", 
    "Display All Books", 
    "Display Statistics",
    "Save & Exit"
])

# ---------- ADD BOOK ----------
if menu == "Add a Book":
    st.subheader("➕ Add a New Book")

    with st.form("add_book_form"):
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        year = st.number_input("Publication Year", min_value=0, max_value=9999, step=1)
        genre = st.text_input("Genre")
        read = st.radio("Have you read this book?", ["Yes", "No"])
        submitted = st.form_submit_button("Add Book")

        if submitted:
            book = {
                "title": title.strip(),
                "author": author.strip(),
                "year": int(year),
                "genre": genre.strip(),
                "read": True if read == "Yes" else False
            }
            st.session_state.library.append(book)
            st.success(f"✅ '{book['title']}' added successfully!")

# ---------- REMOVE BOOK ----------
elif menu == "Remove a Book":
    st.subheader("❌ Remove a Book by Title")
    title = st.text_input("Enter the title of the book to remove")
    if st.button("Remove"):
        removed = remove_by_title(title)
        if removed:
            st.success(f"'{title}' removed successfully!")
        else:
            st.warning(f"No book found with title '{title}'")

# ---------- SEARCH BOOK ----------
elif menu == "Search for a Book":
    st.subheader("🔍 Search Your Library")
    by = st.radio("Search by:", ["Title", "Author"])
    query = st.text_input(f"Enter the {by.lower()} to search")

    if st.button("Search"):
        results = search_books(query, by)
        if results:
            st.success(f"Found {len(results)} matching book(s):")
            for book in results:
                st.markdown(f"- {format_book(book)}")
        else:
            st.warning("No matching books found.")

# ---------- DISPLAY ALL ----------
elif menu == "Display All Books":
    st.subheader("📚 All Books in Your Library")
    display_all_books()

# ---------- STATS ----------
elif menu == "Display Statistics":
    st.subheader("📊 Library Statistics")
    total, percentage = calculate_stats()
    st.write(f"**Total Books:** {total}")
    st.write(f"**Percentage Read:** {percentage:.1f}%")

# ---------- EXIT ----------
elif menu == "Save & Exit":
    save_library(st.session_state.library)
    st.success("✅ Library saved to file successfully!")
    st.info("You can now close this tab or return to another section.")

