import streamlit as st

import src.sidebar_pages as sidebar_pages


# ----- ----- ----- ----- -----


def init_pages_dictionary():
    return sidebar_pages.get_pages()


def main():
    # Render sidebar with pages
    sidebar_pages.render()


if __name__ == "__main__":
    main()
